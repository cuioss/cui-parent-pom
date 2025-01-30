# Commit Policy for Cascade Prompts

This document outlines when automated commits are allowed and when user confirmation is required.

## Core Policy

Cascade will ONLY commit changes automatically when:
1. The task is executing within a Cascade Prompt
2. The Cascade Prompt is defined in README.adoc

For all other scenarios, explicit user confirmation is required before committing changes.

## Verification Process

Before committing any changes, Cascade must:

1. Check Current Context
   - Verify if the task is part of a Cascade Prompt
   - Confirm the prompt source is README.adoc

2. Decision Making
   - If both conditions are met → proceed with automatic commit
   - If either condition is not met → wait for user confirmation

3. Documentation
   - Include reference to the originating Cascade Prompt in commit messages
   - Document any deviations from automatic commit policy

## Rationale

This policy ensures:
- Controlled and documented changes
- Traceability back to defined prompts
- User oversight for non-standard operations
- Consistent commit behavior across repositories

## Scope

This policy applies to:
- All repositories under cuioss organization
- All branches within these repositories
- All types of code changes and documentation updates

## Compliance

To maintain compliance:
1. All Cascade Prompts must be documented in README.adoc
2. Automated commits must reference the originating prompt
3. User confirmation must be obtained for changes outside defined prompts
