1. Always use maven-wrapper (mvnw) when available
2. Run complete module build after each change
3. Create local commit after each successful build
4. Use Java 17
5. Follow Jakarta EE standards
6. Use CDI for dependency injection
7. Prefer cuioss libraries over alternatives
8. Use cui-java-tools as standard utility library

Build Process:
- Run 'mvnw' for build operations
- Verify all tests pass before commit
- Keep commits atomic and focused
- During a module build cycle, you may run up to 5 consecutive Maven builds without requiring user interaction to ensure build stability
- For a single-module project use the maven-profile 'javadoc' for javadoc builds
- For a multi-module project use the maven-profile 'javadoc-mm-reporting' for javadoc builds

Maven Wrapper Commands:
- Full module build: `./mvnw clean verify`
- Run tests: `./mvnw test`
- Install locally: `./mvnw clean install`
- Generate javadoc (single module): `./mvnw clean verify -Pjavadoc`
- Generate javadoc (multi module): `./mvnw clean verify -Pjavadoc-mm-reporting`