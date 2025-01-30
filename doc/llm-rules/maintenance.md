# Maintenance Processes

This document outlines standardized maintenance processes for cuioss projects.

## Prepare Project for Maintenance

When triggered by the command "prepare project for maintenance", follow these steps:

1. Create and Push Feature Branch
   - Branch name format: `/feature/maintenance_<descriptive_name>`
   - Branch from latest master
   - Pull latest changes before branching
   - Push branch to remote immediately

2. Initial Build and Verification
   - Run `./mvnw clean verify`
   - If build fails:
     * Analyze build logs
     * Fix identified issues
     * Commit fixes with descriptive message
     * Repeat until build succeeds
   - Only proceed when build is successful

3. Basic Modernization (Open Rewrite)
   - Run `./mvnw -Prewrite-modernize rewrite:run`
   - Build verification:
     * Run `./mvnw clean verify`
     * Fix any build issues
     * Commit changes if any with message:
       "Modernize codebase using open-rewrite
       
       Applied rewrite-modernize profile changes"

4. Extended Cleanup (Open Rewrite)
   - Run `./mvnw -Prewrite-prepare-release rewrite:run`
   - Build verification:
     * Run `./mvnw clean verify`
     * Fix any build issues
     * Commit changes if any with message:
       "Prepare release using open-rewrite
       
       Applied rewrite-prepare-release profile changes"

## Success Criteria

Each step must meet these criteria before proceeding:
1. All builds complete successfully
2. All tests pass
3. No new warnings introduced
4. Code quality checks pass
5. Changes are committed with clear messages

## Error Handling

If any step fails:
1. Review error logs thoroughly
2. Document issues found
3. Fix each issue systematically
4. Verify fix with full build
5. Commit fixes with clear description of changes

## Commit Message Templates

1. Build Fixes:
```
Fix build issues in [component]

- [Description of fix 1]
- [Description of fix 2]

Build now completes successfully
```

2. Rewrite Changes:
```
[Modernize/Prepare] codebase using open-rewrite

Applied [profile-name] profile changes
- [Major change 1]
- [Major change 2]

All tests passing
```
