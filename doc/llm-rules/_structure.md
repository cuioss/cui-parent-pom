# AI Assistant Rule Processing Structure

## IMMEDIATE ACTION REQUIRED
When ANY user input is received:
1. Check if input starts with "cp:"
   - YES -> STOP and check prompt-list.md FIRST
   - NO -> Continue processing

## COMMAND VALIDATION MAP
Command Type -> Primary File -> Secondary Files

1. cp: persist memory
   - PRIMARY: memory-persistence.md
   - SEQUENCE:
     1. Create branch
     2. Update docs
     3. Update README
     4. Commit
     5. Push/PR

2. cp: fix javadoc
   - PRIMARY: fix-javadoc.md
   - REQUIRES: project.md (build rules)

3. cp: prepare project maintenance
   - PRIMARY: maintenance.md
   - REQUIRES: project.md, technologies.md

4. cp: verify sonar
   - PRIMARY: maintenance.md
   - REQUIRES: project.md (quality gates)

5. cp: execute java maintenance
   - PRIMARY: java-maintenance.md
   - REQUIRES: project.md, technologies.md

6. cp: finalize java maintenance
   - PRIMARY: java-maintenance.md
   - REQUIRES: commit-policy.md

7. cp: verify llm-rules
   - PRIMARY: memory-persistence.md
   - REQUIRES: documentation.md

## CRITICAL RULE DEPENDENCIES
Rule File -> Required Checks

1. project.md
   - ALWAYS check before build commands
   - ALWAYS check before code changes
   - Maven wrapper requirements
   - Build sequence rules

2. commit-policy.md
   - ALWAYS check before git commands
   - Auto-commit restrictions
   - Message format requirements

3. memory-persistence.md
   - ALWAYS check for doc updates
   - Branch naming rules
   - Update sequence

4. documentation.md
   - File format rules
   - Content requirements
   - Reference formats

## ERROR PREVENTION CHECKLIST
STOP and verify if:
1. [ ] Command starts with "cp:" -> Check prompt-list.md
2. [ ] Making git changes -> Check commit-policy.md
3. [ ] Running build -> Check project.md
4. [ ] Updating docs -> Check memory-persistence.md

## SEQUENCE VALIDATIONS
For each action type, verify in order:

1. Commands:
   a. Validate in prompt-list.md
   b. Load primary file
   c. Check dependencies
   d. Execute sequence

2. Code Changes:
   a. Check project.md
   b. Verify technologies.md
   c. Review commit-policy.md
   d. Execute change

3. Documentation:
   a. Load memory-persistence.md
   b. Check documentation.md
   c. Verify README.adoc
   d. Execute update

## RESPONSE TEMPLATE
For each user interaction:
```
1. Command Validation:
   - Is it a cp: command? [YES/NO]
   - If YES: Verified in prompt-list.md? [YES/NO]

2. Action Classification:
   - Type: [COMMAND/CODE/DOCS/BUILD]
   - Primary File: [filename.md]
   - Required Files: [list]

3. Execution Checklist:
   - [ ] Validated command format
   - [ ] Checked primary file
   - [ ] Verified dependencies
   - [ ] Confirmed sequence

4. Response:
   [action details]
```

## COMMON FAILURE POINTS
STOP and RECHECK if:
1. Assuming command format
2. Skipping primary file check
3. Missing dependency verification
4. Incomplete sequence validation

## VERSION CONTROL
ALWAYS verify:
1. Branch requirements
2. Commit message format
3. Change scope
4. User confirmation needs

## BUILD PROCESS
ALWAYS check:
1. Maven wrapper usage
2. Build command format
3. Module-specific rules
4. Test requirements

## DOCUMENTATION UPDATES
ALWAYS verify:
1. Branch naming
2. File location
3. Content format
4. Cross-references
