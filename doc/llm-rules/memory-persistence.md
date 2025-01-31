# Memory Persistence Process

This document outlines the process for persisting and updating memory rules in the repository.

## Process Overview

When triggered by the prompt "cp: persist memory", follow these steps:

1. Create Feature Branch (if needed)
   - Branch name format: `/feature/memory_<descriptive_name>`
   - Branch from latest master
   - Pull latest changes before branching

2. Update Documentation
   - Identify relevant `.md` files in `doc/llm-rules/`
   - Make necessary updates or create new files
   - Ensure changes follow documentation guidelines
   - Verify all references exist

3. Update README.adoc
   - Maintain list of available Cascade Prompts
   - Update memory files overview
   - Add new prompts to the command table
   - Keep file descriptions current

4. Commit Changes
   - Add modified files
   - Use clear, descriptive commit message
   - Include overview of changes
   - Reference related documentation

5. Push Changes
   - Push feature branch to remote
   - Command: git push -u origin <branch_name>
   - Verify push was successful

6. Create Pull Request (if needed)
   - Title: Clear description of memory updates
   - Body should include:
     * Overview of changes
     * Detailed list of updates by category
     * Validation steps taken
     * Impact of changes

## File Organization

Memory rules are organized in topic-specific files:
- `README.adoc`: Overview of prompts and memory files
- `documentation.md`: Documentation standards and practices
- `logging.md`: Logging conventions and tools
- `project.md`: Build and project structure rules
- `technologies.md`: Core technology stack
- `testing.md`: Testing frameworks and practices
- `memory-persistence.md`: This file - process for updating memories

## Validation Requirements

Before submitting changes:
1. Verify all references exist
2. Ensure no speculative features
3. Maintain consistent terminology
4. Follow documentation structure
5. Keep changes focused and atomic
6. Verify README.adoc is updated
7. Check Cascade Prompt documentation is complete

## Pull Request Template

```markdown
## Overview
[Brief description of memory updates]

### Changes
[Category 1]
- Change detail 1
- Change detail 2

[Category 2]
- Change detail 1
- Change detail 2

### README Updates
- [ ] Added new Cascade Prompts
- [ ] Updated memory files overview
- [ ] Updated file descriptions

### Validation
- All additions based on existing practices
- No speculative features added
- All references verified
- Consistent terminology maintained
- README.adoc properly updated
```

## Cascade Prompt Structure

The "cp: persist memory" prompt ensures:
1. Documentation is properly organized and maintained
2. README.adoc reflects all available prompts and memory files
3. Changes are properly tracked and reviewed
4. Documentation remains consistent and accurate
