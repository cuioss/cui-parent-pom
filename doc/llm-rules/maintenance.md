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

## Execute Java Maintenance

When triggered by the command "execute java maintenance", follow these steps:

1. Precondition Verification
   - Verify current branch is a feature branch
   - Run `./mvnw clean verify` to ensure successful build
   - Check for uncommitted changes (must be none)
   - Only proceed if all preconditions are met

2. Project Analysis
   - Analyze overall project structure
   - Identify all modules
   - Document dependencies and relationships
   - Note areas needing special attention
   - Document current API surface
   - Review existing dependencies

3. Critical Constraints
   - API Stability:
     * Must preserve existing public API
     * No changes to method signatures
     * No changes to class hierarchies
     * No changes to package structure
     * No removal or modification of public methods
     * No changes to method return types or parameters
   
   - Dependency Management:
     * No new dependencies may be added
     * This constraint takes precedence over CUI standards
     * Must work within existing dependency set
     * Cannot add CUI dependencies if not already present

4. Module-by-Module Maintenance
   For each module, perform these steps:

   a. Module Analysis
      - Review module structure and purpose
      - Identify all Java packages
      - Document module-specific requirements
      - Document current dependencies
      - Map public API surface

   b. Package-Level Maintenance
      For each Java package:

      1. Test Refactoring
         - Refactor unit tests to CUI standards where possible within dependency constraints:
           * Use JUnit 5 if already available
           * Use existing test utilities
           * Implement @ParameterizedTest where possible with existing dependencies
         - Add/extend tests for better coverage:
           * Focus on error scenarios
           * Test all log levels
           * Verify edge cases
         - Build and verify:
           * Run `./mvnw clean verify`
           * Fix any issues
           * Commit with message:
             "Refactor tests in [package] to CUI standards
             
             - Enhanced test coverage
             - Added error scenario tests
             - Maintained existing dependencies"

      2. Code Refactoring
         - Apply CUI coding standards within constraints:
           * Use CuiLogger only if already available
           * Maintain existing API contracts
           * Apply proper exception handling
           * Use only existing utility classes
         - Build and verify:
           * Run `./mvnw clean verify`
           * Fix any issues
           * Commit with message:
             "Refactor code in [package] to CUI standards
             
             - Enhanced error handling
             - Applied coding standards
             - Maintained API stability
             - No dependency changes"

      3. Documentation Update
         - Update documentation to CUI standards:
           * Verify all references exist
           * Use proper linking
           * Include code examples from tests
           * Document all parameters and returns
         - Build javadoc:
           * Run `./mvnw javadoc:javadoc`
           * Fix any warnings/errors
           * Commit with message:
             "Update documentation in [package] to CUI standards
             
             - Enhanced javadoc
             - Added code examples
             - Fixed references
             - Maintained API documentation"

## SonarCloud Verification

When triggered by the command "verify sonar", follow these steps:

1. Identify Current Branch
   ```bash
   git rev-parse --abbrev-ref HEAD
   ```

2. Access SonarCloud Analysis
   - URL format: https://sonarcloud.io/dashboard?id=cuioss_<project-name>&branch=<current_branch_name>

3. Review Results:
   - Check quality gate status
   - Review any new issues
   - Verify code coverage metrics
   - Examine security vulnerabilities

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

3. Test Refactoring:
```
Refactor tests in [package] to CUI standards

- Enhanced test coverage for [areas]
- Added error scenario tests for [components]
- Improved assertions and validations
- Maintained existing dependencies
- No new dependencies added

Coverage increased to XX%
```

4. Code Refactoring:
```
Refactor code in [package] to CUI standards

- Enhanced error handling for [scenarios]
- Applied coding standards within constraints
- Maintained API stability
- No dependency changes
- Improved [specific improvements]

All tests passing
```

5. Documentation Updates:
```
Update documentation in [package] to CUI standards

- Enhanced javadoc for [classes/methods]
- Added code examples from unit tests
- Fixed and verified all references
- Added missing parameter documentation
- Maintained API documentation

Javadoc builds without warnings
```
