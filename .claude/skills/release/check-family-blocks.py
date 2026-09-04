#!/usr/bin/env python3
"""Check that every requireSameVersions family block is still satisfiable.

The blocks in the root pom's `mojo-enforcer-rules` execution assert that a set of
artifacts always resolves to one version. That assertion is only legitimate while the
artifacts really are one release train. When an upstream groupId turns out to carry two
independently versioned lines, the block becomes impossible to satisfy: no
dependencyManagement pin can reconcile versions that were never published in common.

This repo cannot notice that on its own. It is a POM/BOM aggregator, so its own build
resolves none of these artifacts and stays green while every consumer breaks.

The check is therefore pure Maven Central metadata: for each block, intersect the
published version sets of its artifacts. An empty intersection means the block is
unsatisfiable and ships a broken parent to every consumer.

    exit 0  every block satisfiable (module-only patch notes are informational)
    exit 1  at least one block unsatisfiable
    exit 2  could not determine - also blocking, an unresolvable check is not a pass
"""

import argparse
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CENTRAL = "https://repo1.maven.org/maven2"
POM_NS = "{http://maven.apache.org/POM/4.0.0}"
TIMEOUT = 30

# Blocks knowingly left wildcarded, with the reason. A waived block is reported but does
# not fail the run. Keep the reason current: a waiver is a decision, not a silence.
WAIVERS = {
    "io.smallrye.config:*": (
        "smallrye-config-jasypt (3.17.2) and smallrye-config-converter-json (3.8.3, "
        "discontinued) lag the 3.18.2 core. Neither is on the Quarkus default path, so "
        "the block is left broad deliberately; narrow it if either becomes reachable."
    ),
}


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as response:
            return response.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError):
        return None


def versions_of(coord):
    """Published versions of 'groupId:artifactId', or None when Central has no metadata."""
    group, artifact = coord.split(":", 1)
    body = fetch(f"{CENTRAL}/{group.replace('.', '/')}/{artifact}/maven-metadata.xml")
    if body is None:
        return None
    return set(re.findall(r"<version>([^<]+)</version>", body))


def artifacts_in_group(group):
    """Artifact ids published under a groupId, read off the Central directory index."""
    body = fetch(f"{CENTRAL}/{group.replace('.', '/')}/")
    if body is None:
        return None
    names = re.findall(r'href="([^"/]+)/"', body)
    return sorted(n for n in names if n != "..")


def read_blocks(pom_path):
    """The requireSameVersions dependency patterns, one list per block, in pom order."""
    root = ET.parse(pom_path).getroot()
    blocks = []
    for rule in root.iter(f"{POM_NS}requireSameVersions"):
        deps = rule.find(f"{POM_NS}dependencies")
        if deps is None:
            continue  # a plugins-only block, not an artifact family
        patterns = [e.text.strip() for e in deps if e.text and e.text.strip()]
        if patterns:
            blocks.append(patterns)
    return blocks


def expand(patterns):
    """Resolve patterns to concrete coordinates. Returns (coords, unresolved_patterns)."""
    coords, unresolved = [], []
    for pattern in patterns:
        if "*" not in pattern:
            coords.append(pattern)
            continue
        group = pattern.split(":", 1)[0]
        found = artifacts_in_group(group)
        if found is None:
            unresolved.append(pattern)
        else:
            coords.extend(f"{group}:{a}" for a in found)
    return coords, unresolved


def newest(versions):
    """Newest version by Maven-ish ordering. Good enough for reporting, not for gating."""
    def key(v):
        return [int(p) if p.isdigit() else p for p in re.split(r"[.\-]", v)]

    try:
        return max(versions, key=key)
    except TypeError:  # mixed numeric/alpha segments
        return sorted(versions)[-1]


def check_block(patterns):
    """Returns (status, lines) where status is 'ok' | 'unsatisfiable' | 'unknown'."""
    label = ", ".join(patterns)
    coords, unresolved = expand(patterns)
    if unresolved:
        return "unknown", [f"  could not enumerate: {', '.join(unresolved)}"]

    with ThreadPoolExecutor(max_workers=12) as pool:
        results = dict(zip(coords, pool.map(versions_of, coords)))

    missing = [c for c, v in results.items() if v is None]
    present = {c: v for c, v in results.items() if v}
    if not present:
        return "unknown", [f"  no metadata for any artifact in {label}"]

    common = set.intersection(*present.values())
    lines = [f"  {len(present)} artifacts" + (f", {len(missing)} without metadata" if missing else "")]

    if not common:
        # Name the artifacts that break the intersection: those sharing no version with
        # the largest coherent group.
        anchor = max(present.values(), key=len)
        outliers = [c for c, v in present.items() if not (v & anchor)]
        lines.append("  NO COMMON VERSION - this block cannot be satisfied by any pin")
        for c in sorted(outliers):
            lines.append(f"    outlier: {c} -> {newest(present[c])}")
        return "unsatisfiable", lines

    top = newest(common)
    overall = newest(set().union(*present.values()))
    lines.append(f"  newest common version: {top}")

    # Artifacts that never published the family's newest version cap the common version.
    # A single capped-out module is an out-of-band patch elsewhere (bcprov-jdk18on 1.85.2);
    # a large group of them is a shrinking family (RESTEasy dropped its netty/vertx modules
    # in 7.x). Neither is a failure - both are worth seeing before a release.
    if overall != top:
        cappers = sorted(c for c, v in present.items() if overall not in v)
        shown = ", ".join(f"{c.split(':')[1]} ({newest(present[c])})" for c in cappers[:5])
        more = f" +{len(cappers) - 5} more" if len(cappers) > 5 else ""
        lines.append(f"  family newest is {overall}; {len(cappers)} artifact(s) never "
                     f"published it, capping the common version")
        lines.append(f"    {shown}{more}")
    return "ok", lines


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=".", help="path to the cui-parent-pom checkout")
    args = parser.parse_args()

    pom = Path(args.repo).expanduser() / "pom.xml"
    if not pom.is_file():
        print(f"no pom.xml at {pom}", file=sys.stderr)
        return 2

    blocks = read_blocks(pom)
    if not blocks:
        print("no requireSameVersions dependency blocks found - pom layout changed?",
              file=sys.stderr)
        return 2

    failed = unknown = 0
    for patterns in blocks:
        label = ", ".join(patterns) if len(patterns) <= 2 else \
            f"{patterns[0].split(':')[0]}:* ({len(patterns)} artifacts enumerated)"
        status, lines = check_block(patterns)
        waiver = next((WAIVERS[p] for p in patterns if p in WAIVERS), None)

        if status == "unsatisfiable" and waiver:
            mark = "WAIVED"
        elif status == "unsatisfiable":
            mark = "BROKEN"
            failed += 1
        elif status == "unknown":
            mark = "UNKNOWN"
            unknown += 1
        else:
            mark = "OK"

        print(f"[{mark}] {label}")
        for line in lines:
            print(line)
        if waiver and status == "unsatisfiable":
            print(f"  waiver: {waiver}")
        print()

    if failed:
        print(f"{failed} block(s) unsatisfiable - narrow them to the artifacts that "
              f"genuinely share a version before releasing")
        return 1
    if unknown:
        print(f"{unknown} block(s) could not be determined - resolve before releasing")
        return 2
    print("all requireSameVersions blocks satisfiable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
