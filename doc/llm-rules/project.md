# Project Configuration and Build Rules

## Type: Rules
## Related Files: 
- `java-maintenance.md`: For Java-specific configurations
- `technologies.md`: For technology standards
- `memory-persistence.md`: For documentation updates

## Commands: 
- `cp: prepare project maintenance`
- `cp: execute java maintenance`

## Overview
This document defines the core project configuration and build rules for CUI OSS projects.

## Build Rules

### Maven Wrapper Usage
1. Always use maven-wrapper (mvnw) when available
2. Run complete module build after each change
3. Create local commit after each successful build

### Build Optimization
1. During build and fix cycles in multi-module projects:
   - Use `-rf :module-name` to resume from specific module
   - Only build affected module and downstream dependencies
   - Example: `./mvnw clean verify -rf :module-name`

2. Build Command Format:
   - Full build: `./mvnw clean verify`
   - Module build: `./mvnw clean verify -rf :module-name`
   - Test only: `./mvnw test`
   - Install: `./mvnw clean install`

3. Build Sequence Rules:
   - Verify all tests pass before commit
   - Keep commits atomic and focused
   - Run up to 5 consecutive builds without user interaction
   - Use javadoc profile as needed:
     * Single module: `-Pjavadoc`
     * Multi-module: `-Pjavadoc-mm-reporting`

### Additional Rules
4. Use Java 17
5. Follow Jakarta EE standards
6. Use CDI for dependency injection
7. Prefer cuioss libraries over alternatives
8. Use cui-java-tools as standard utility library