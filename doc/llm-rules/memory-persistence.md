# Memory Persistence Process

This document outlines the process for persisting and updating memory rules in the repository.

## Process Overview

When triggered by the command "persist memory to repo", follow these steps:

1. Create Feature Branch
   - Branch name format: `/feature/memory_<descriptive_name>`
   - Branch from latest master
   - Pull latest changes before branching

2. Update Documentation
   - Identify relevant `.md` files in `doc/llm-rules/`
   - Make necessary updates or create new files
   - Ensure changes follow documentation guidelines
   - Verify all references exist

3. Commit Changes
   - Add modified files
   - Use clear, descriptive commit message
   - Include overview of changes
   - Reference related documentation

4. Create Pull Request
   - Title: Clear description of memory updates
   - Body should include:
     * Overview of changes
     * Detailed list of updates by category
     * Validation steps taken
     * Impact of changes

## File Organization

Memory rules are organized in topic-specific files:
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

### Validation
- All additions based on existing practices
- No speculative features added
- All references verified
- Consistent terminology maintained
```
