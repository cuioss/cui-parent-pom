# Cascade Prompt List Command

When triggered by the command "cp", the following numbered list of available prompts will be displayed:

1. `cp: fix javadoc`
   - Fixes Javadoc errors and warnings
   - Makes minimal modifications
   - Preserves content

2. `cp: prepare project maintenance`
   - Creates feature branch
   - Performs initial verification
   - Sets up maintenance context

3. `cp: verify sonar`
   - Reviews quality gates
   - Examines new issues
   - Verifies coverage metrics

4. `cp: persist memory`
   - Updates documentation rules
   - Maintains consistency
   - Updates README.adoc

5. `cp: execute java maintenance`
   - Updates dependencies
   - Applies code cleanup
   - Improves code quality

6. `cp: finalize java maintenance`
   - Runs OpenRewrite recipes
   - Verifies build stability
   - Prepares pull request

7. `cp: verify llm-rules`
   - Checks consistency
   - Updates documentation
   - Ensures completeness

## Usage

1. Enter command "cp" to display this numbered list
2. Enter the number corresponding to the desired prompt
3. The selected prompt will be executed with its full workflow

## Implementation Notes

- Numbers must be entered exactly as shown
- Invalid numbers will be rejected
- The prompt list is fixed and maintained in documentation
- All prompts follow their defined workflows
- User confirmation may be required based on prompt type
