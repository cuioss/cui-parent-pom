---
name: release
description: Cut a cui-parent-pom release — bump .github/project.yml version and the README sample version, open and merge the release PR, wait for the automated Release workflow, verify the release landed, then reformat the generated GitHub release notes
user-invocable: true
allowed-tools: Bash, Read, Edit
---

# Release Skill

Cuts a new `cui-parent-pom` (`de.cuioss:cui-parent-pom`) release end-to-end: determine the
version, open the version-bump PR that triggers the release, merge it, wait for the automated
Release workflow, verify the release landed, and reformat the auto-generated GitHub release
notes.

## How the release is wired (read first)

The release is **fully automated by GitHub Actions**. `.github/workflows/release.yml` triggers
on a **merged pull request that changes `.github/project.yml`**:

```yaml
on:
  pull_request:
    types: [closed]
    paths:
      - '.github/project.yml'
```

So this skill never runs Maven release goals by hand. Its job is to produce and merge the
correct `project.yml` change; the reusable `cuioss-organization` release workflow
(`reusable-maven-release.yml`, run with the `release-pom` profile) does the Maven release
(`-DreleaseVersion=<current-version> -DdevelopmentVersion=<next-version>`), tagging, Maven
Central deploy, GitHub release creation, and — because `pages.deploy-at-release: true` — the
documentation pages deploy.

This is a **POM-and-BOM aggregator** — there is no Java source, no tests, and no
integration/e2e suites. The only PR gating check is the **Maven Build** matrix (Java 21).

Observed timings:
- PR gating check (**Maven Build**): typically **~1–3 min** (validate + enforcer only, no tests).
- Release workflow: **~5 min**, but Maven Central propagation, the GitHub release publish, and
  the pages deploy can lag → allow **up to ~30 min** before treating it as stuck.

## Version scheme (differs from library repos)

Read the release block in `.github/project.yml`:
- `release.current-version` — the last released version, e.g. `1.4.5`
- `release.next-version` — the rolling development version, held at `1.4-SNAPSHOT`

**Default rule — patch bump.** The tag history is `1.4.0, 1.4.1, … 1.4.5`, and `next-version`
stays `1.4-SNAPSHOT` across releases (the pom `<version>` is `1.4-SNAPSHOT`). To cut the next
release, **increment the third segment of `current-version`** (`1.4.5` → `1.4.6`) and **leave
`next-version` at `1.4-SNAPSHOT`**. Do **not** strip `-SNAPSHOT` from `next-version`
(that would produce a lower version like `1.4`).

**Ask the user** (AskUserQuestion) only if in doubt — e.g. a new minor line (`1.5.0`) or a
major bump is intended, or `current-version`/tags look inconsistent. Otherwise state the
determined version and proceed.

## Workflow

### Step 1 — Determine the version number
From `project.yml`: release version = `current-version` with patch+1 (e.g. `1.4.6`).
`next-version` is unchanged (`1.4-SNAPSHOT`).

### Step 2 — Determine current status (clean to release?)
```bash
gh pr list --repo cuioss/cuioss-parent-pom --state open --json number,title,isDraft
```
- **No open PRs** → proceed.
- **Open PRs exist** → surface the list and **ask the user** whether to proceed or wait. Do
  not silently ignore them.

Confirm the working tree is clean (`git status --porcelain`) before branching.

### Step 3 — Pull current main
```bash
git checkout main && git pull --ff-only origin main
```

### Step 4 — Create the release branch
Branch prefix **must** be a CI-accepted prefix (`main`, `feature/*`, `fix/*`, `chore/*`,
`release/*`, `dependabot/**`) or the Maven Build check skips and auto-merge is blocked:
```bash
git checkout -b chore/release_<version>   # e.g. chore/release_1.4.6
```

### Step 5 — Update `.github/project.yml` and the README sample version
1. Edit the `release` block in `.github/project.yml`:
   - `current-version:` → the release version from Step 1 (e.g. `1.4.6`)
   - `next-version:` → **unchanged** (`1.4-SNAPSHOT`)
2. Update the parent-version sample in **`README.adoc`** (the `<version>…</version>` under the
   `cui-java-parent` `<parent>` in the "Usage for Standard java-modules" snippet) to the new
   release version, so the published docs show the released parent version. Then check for any
   other stale references to the previous version in docs:
   ```bash
   grep -rn "<previous-version>" --include="*.adoc" .   # e.g. 1.4.5 — update sample references
   ```
   Do **not** touch `version.cui.parent` in `pom.xml` — the release plugin bumps it
   automatically via `preparationGoals`.

### Step 6 — Commit, push, open PR
```bash
git add .github/project.yml README.adoc
git commit -m "chore(release): prepare release <version>"
git push -u origin chore/release_<version>
gh pr create --repo cuioss/cuioss-parent-pom --base main \
  --title "chore(release): prepare release <version>" \
  --label "skip-bot-review" \
  --body "Bump current-version to <version> (next-version stays <next-version>) and the README parent sample. Triggers the automated Release workflow on merge."
```
Apply the **`skip-bot-review`** label (via `--label "skip-bot-review"` on `gh pr create`, or
`gh pr edit <pr#> --add-label "skip-bot-review"` if the PR already exists). A mechanical
release-prep PR only changes the `project.yml` version and the README sample — no bot review is
necessary, and the label suppresses the automated reviewers (CodeRabbit / Sourcery).

Commit trailer: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model name, no
"Generated with Claude Code" footer).

### Step 7 — Wait for PR checks (~1–3 min)
```bash
gh pr checks <pr#> --repo cuioss/cuioss-parent-pom --watch
```

### Step 8 — Handle PR comments / failures (if any)
- If a check fails, read the failing run's log (`gh run view <id> --log-failed`), fix on the
  branch, push, re-wait. **Never** merge a red PR.
- If the automated reviewer or a human leaves comments (`gh pr view <pr#> --comments`), address
  them per the PR-comment protocol in `CLAUDE.md`: reply to and resolve every comment; ask the
  user when uncertain.

### Step 9 — Merge → release starts automatically
`main` is governed by the org-managed **merge queue** (`main-merge-queue`), so the merge is
**enqueued, not immediate**, and `--delete-branch` is **rejected** (the queue auto-deletes the
head branch). Do **not** pass `--delete-branch`:
```bash
gh pr merge <pr#> --repo cuioss/cuioss-parent-pom --squash
```
This only *queues* the PR. Poll until it actually lands on `main` — the release fires on the
merge commit, not on enqueue (the queue can take a few minutes):
```bash
gh pr view <pr#> --repo cuioss/cuioss-parent-pom --json state --jq .state   # wait for MERGED
```
Merging this PR (it touches `.github/project.yml`) fires `release.yml` automatically — do
**not** dispatch the release manually unless the auto-trigger demonstrably did not fire.

> The release workflow itself is unaffected by the queue: `cuioss-release-bot` is a bypass
> actor on `main-merge-queue`, so its direct push of the release commit + tag succeeds.

### Step 10 — Wait for the Release workflow (~30 min)
```bash
gh run list --repo cuioss/cuioss-parent-pom --workflow "Release" --limit 3 \
  --json status,conclusion,displayTitle,databaseId
gh run watch <databaseId> --repo cuioss/cuioss-parent-pom
```

### Step 11 — Verify the release landed
```bash
gh release view <version> --repo cuioss/cuioss-parent-pom --json tagName,name,createdAt,body
git fetch --tags && git tag --list <version>
```
Confirm the tag exists and a GitHub release for `<version>` was created. If not, inspect the
Release workflow run log before proceeding.

### Step 12 — Reformat the generated release notes
The Release workflow creates the GitHub release with **auto-generated** notes (a flat
`## What's Changed` list). Rewrite them in place using the house format below, then push:
```bash
mkdir -p .plan/temp
gh release view <version> --repo cuioss/cuioss-parent-pom --json body --jq .body > .plan/temp/release-<version>-orig.md
# ...build the reformatted body in .plan/temp/release-<version>.md...
gh release edit <version> --repo cuioss/cuioss-parent-pom --notes-file .plan/temp/release-<version>.md
```

#### House format rules (apply exactly)
1. **Two top-level groups:** `## Features & Enhancements` and `## Dependency Updates`.
2. **Features & Enhancements** — for a POM/BOM aggregator these are rare; group functional PRs
   by theme with `###` subheadings when present, e.g. `### Build & Configuration`,
   `### CI/CD & Workflows`, `### Documentation`. Omit empty sections.
3. **Dependency Updates** — group by type with `###` subheadings:
   - `### Java` — managed library version bumps in the BOMs (e.g. quarkus, myfaces, jakarta,
     microprofile, cui-java-tools, cui-http)
   - `### Infra` — build/CI: build-plugin bumps, `cuioss-organization` workflow bumps,
     GitHub Actions bumps
4. **Collapse version chains** — when the same artifact is bumped multiple times (`A → B → C`),
   keep one entry spanning the full range (`A → C`).
5. **Remove all OpenRewrite bumps and friends** — drop every `rewrite-maven-plugin`,
   `rewrite-migrate-java`, `rewrite-testing-frameworks`, and related OpenRewrite PR.
6. **Remove internal tooling churn** — drop PRs that only touch dev/build orchestration with no
   user-facing effect, and the mechanical version-bump PR itself.
7. Preserve each kept PR line verbatim (`* <title> by @author in <url>`); merge duplicate
   titles onto one line with both URLs.
8. Keep the trailing `**Full Changelog**: ...compare/<prev>...<version>` line.

### Step 13 — Done
Report: released version, release URL, the PR number, and how many dependency PRs were
collapsed/removed during note reformatting.

## Critical rules
- The release is triggered by **merging a `.github/project.yml` change** — never hand-run Maven
  release goals.
- **Patch-bump `current-version`; keep `next-version` at `1.4-SNAPSHOT`.**
- Always update the **README parent sample version** in the same PR; never touch
  `version.cui.parent` (auto-bumped by the release plugin).
- Branch prefix **must** be `chore/` (or another CI-accepted prefix) or the build check skips
  and auto-merge is blocked.
- Never merge a red PR; fix and re-wait.
- Temporary files go under `.plan/temp/`.
- Commit trailer: `Co-Authored-By: Claude <noreply@anthropic.com>`; no PR footer line.
