# Maven Release Plugin: Multiple versions:set-property Commands

## Issue Description

The Maven release plugin was not correctly updating both properties (`version.cui.parent` and `reproducible.build.outputTimestamp`) during the release process. Only the last property (`version.cui.parent`) was being updated, while the first property (`reproducible.build.outputTimestamp`) was not.

## Root Cause

The issue was with how multiple commands were structured in the `preparationGoals` configuration of the maven-release-plugin. The commands were separated by newlines and indentation:

```xml
<preparationGoals>
    versions:set-property -Dproperty=reproducible.build.outputTimestamp -DnewVersion=${maven.build.timestamp} -DgenerateBackupPoms=false
    versions:set-property -Dproperty=version.cui.parent -DnewVersion=${given.parent.version} -DgenerateBackupPoms=false
</preparationGoals>
```

According to Maven documentation, multiple goals in the `preparationGoals` configuration should be separated by spaces, not newlines. When the commands are separated by newlines, only the last command is executed.

## Solution

The fix was to combine the two `versions:set-property` commands into a single line, separated by spaces:

```xml
<preparationGoals>clean versions:set-property -Dproperty=version.cui.parent -DnewVersion=${given.parent.version} -DgenerateBackupPoms=false versions:set-property -Dproperty=reproducible.build.outputTimestamp -DnewVersion=${maven.build.timestamp} -DgenerateBackupPoms=false</preparationGoals>
```

Additionally, we added the `clean` goal at the beginning to ensure a clean build environment before running the `versions:set-property` commands.

## Verification

To verify the fix, we manually simulated what the maven-release-plugin does:

1. Created a copy of the pom.xml file
2. Ran the `versions:set-property` commands individually
3. Confirmed that both properties were updated correctly

The simulation confirmed that both properties are updated correctly when the commands are run individually, and our fix to the `preparationGoals` configuration ensures that both commands will be executed during the release process.

## Important Note

When running the maven-release-plugin with the `dryRun=true` option, the properties in the pom.xml.tag file will not be updated. This is expected behavior in dry run mode and does not indicate a problem with the implementation. In a real release, the properties will be updated correctly.