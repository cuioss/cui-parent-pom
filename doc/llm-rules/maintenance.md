# Maintenance Processes

This document outlines standardized maintenance processes for cuioss projects.

## Prepare Project for Maintenance Preparation

When triggered by the command "cp: prepare project maintenance", follow these steps:

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

When triggered by the command "cp: execute java maintenance", follow these steps:

1. Precondition Verification
   - Verify current branch is a feature branch
   - Run `./mvnw clean verify` to ensure successful build
   - Check for uncommitted changes (must be none)
   - Only proceed if all preconditions are met

2. Progress Tracking Initialization
   - Check for existing java-maintenance.md
   - If exists:
     * Read current progress
     * Verify state matches (branch, module, package)
     * Resume from last successful step
   - If not exists:
     * Create new java-maintenance.md
     * Initialize with current timestamp
     * Set status to "In Progress"
     * Record current branch

3. Project Analysis
   - Analyze overall project structure
   - Identify all modules
   - Document dependencies and relationships
   - Note areas needing special attention
   - Document current API surface
   - Review existing dependencies
   - Update progress file with module list

4. Critical Constraints
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

5. Module-by-Module Maintenance
   For each module, perform these steps:

   a. Module Analysis
      - Review module structure and purpose
      - Identify all Java packages
      - Document module-specific requirements
      - Map public API surface

   b. Package-Level Maintenance
      For each Java package:

      1. Test Refactoring
         - Update progress file with current phase "Test Refactoring"
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
           * On success:
             - Update progress file with completion
             - Commit with message:
               "Refactor tests in [package] to CUI standards
               
               - Enhanced test coverage
               - Added error scenario tests
               - Maintained existing dependencies"

      2. Code Refactoring
         - Update progress file with current phase "Code Refactoring"
         - Apply CUI coding standards within constraints:
           * Use CuiLogger only if already available
           * Maintain existing API contracts
           * Apply proper exception handling
           * Use only existing utility classes
         - Build and verify:
           * Run `./mvnw clean verify`
           * Fix any issues
           * On success:
             - Update progress file with completion
             - Commit with message:
               "Refactor code in [package] to CUI standards
               
               - Enhanced error handling
               - Applied coding standards
               - Maintained API stability
               - No dependency changes"

      3. Documentation Update
         - Update progress file with current phase "Documentation Update"
         - Update documentation to CUI standards:
           * Verify all references exist
           * Use proper linking
           * Include code examples from tests
           * Document all parameters and returns
         - Build javadoc:
           * Run `./mvnw javadoc:javadoc`
           * Fix any warnings/errors
           * On success:
             - Update progress file with completion
             - Commit with message:
               "Update documentation in [package] to CUI standards
               
               - Enhanced javadoc
               - Added code examples
               - Fixed references
               - Maintained API documentation"

      4. Package Completion
         - Update progress file marking package as complete
         - Record all completed phases
         - Add timestamp for completion

6. Module Completion
   - Update progress file marking module as complete
   - Record timestamp for module completion
   - Verify all packages are processed
   - Add module to completed modules list

7. Process Completion
   - After all modules are complete:
     * Update progress file status to "Completed"
     * Add final completion timestamp
     * Archive progress file with completion date

## SonarCloud Verification

When triggered by the command "cp: verify sonar", follow these steps:

### 1. Access Process

#### Get Current Branch
```bash
git rev-parse --abbrev-ref HEAD
```

#### Access Points
- Dashboard View:
  ```
  https://sonarcloud.io/dashboard?id=cuioss_<project-name>&branch=<branch-name>
  ```
- Issues API:
  ```
  https://sonarcloud.io/api/issues/search?componentKeys=cuioss_<project-name>&branch=<branch-name>&resolved=false&sinceLeakPeriod=true
  ```

### 2. Review Requirements

#### Quality Gate Status
- Check overall status
- Review failing conditions
- Note any quality metric thresholds

#### Issue Analysis
Review issues by:
- Severity (MAJOR, MINOR, etc.)
- Type (CODE_SMELL, BUG, VULNERABILITY)
- Impact on quality metrics
- Associated code locations
- Rule references

#### Code Coverage Review
- Overall coverage percentage
- New code coverage
- Uncovered lines
- Critical areas lacking coverage

#### Security Assessment
- Check for vulnerabilities
- Review security hotspots
- Assess security-related code smells

### 3. Documentation Requirements

When documenting findings:
1. File and line references must be precise
2. Include issue descriptions from SonarCloud
3. Note severity and impact levels
4. Document any suggested remediation steps
5. Reference specific SonarCloud rules when applicable

### 4. Integration Points

1. Regular Review Points:
   - After major feature completion
   - Before creating pull requests
   - During code review process
   - Post-merge verification

2. Response Requirements:
   - Address all new issues promptly
   - Document intentional deviations
   - Track technical debt decisions
   - Update related documentation

### 5. Success Criteria

A successful SonarCloud review should:
1. Identify all new issues
2. Assess impact on code quality
3. Provide clear remediation paths
4. Document findings appropriately
5. Integrate with existing quality processes

## Finalize Java Maintenance

When triggered by the command "cp: finalize java maintenance", follow these steps:

### 1. Precondition Verification
Before proceeding, verify all preconditions are met:
- Current branch is a feature branch (not master/main)
- Project builds successfully with `./mvnw clean verify`
- No uncommitted changes exist in the working directory

If any precondition fails:
- Report the specific failure
- Provide guidance for resolution
- Do not proceed until all conditions are met

### 2. OpenRewrite Cleanup
Execute extended cleanup using OpenRewrite:
```bash
./mvnw -Prewrite-prepare-release rewrite:run
```

### 3. Build Verification
- Run full build: `./mvnw clean verify`
- If build fails:
  * Analyze build logs
  * Fix identified issues
  * Repeat build until successful
- Do not proceed if build cannot be fixed

### 4. Change Management
If OpenRewrite made changes:
- Review changes for correctness
- Create descriptive commit message
- Commit all changes

### 5. Pull Request Creation
- Create pull request from feature branch to master
- Include in PR description:
  * Summary of OpenRewrite changes
  * Build verification results
  * Any manual fixes applied

### Success Criteria
- All preconditions met
- OpenRewrite cleanup completed
- Build passes successfully
- Changes (if any) committed
- Pull request created

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
