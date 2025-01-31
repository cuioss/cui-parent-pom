1. Use CuiLogger with constant name 'LOGGER'
2. Never use log4j or slf4j
3. Never use System.out or System.err - always use appropriate logger level
4. Exception parameter always comes first in log methods
5. Use '%s' for string substitutions (not '{}')
6. Use de.cuioss.tools.logging.LogRecord for template logging
7. Use cui-test-juli-logger for testing
8. Use de.cuioss.test.juli.TestLogLevel for log levels in tests

Implementation Notes:
- LogRecord API: https://github.com/cuioss/cui-java-tools/tree/master/src/main/java/de/cuioss/tools/logging
- Use LogRecord#format for parameterized log messages
- For LogAsserts testing, use LogRecord#resolveIdentifierString()
- Logger should be private static final

Testing Guidelines:
1. Test Coverage Requirements:
   - Test coverage required for INFO/WARN/ERROR/FATAL logs in production code
   - No need to verify logs from within unit tests themselves
   - Test parameter substitution
   - Test exception logging
   - Test template-based logging with LogRecord

2. LogAsserts Usage:
   - First argument must be TestLogLevel
   - Only assertNoLogMessagePresent needs Logger parameter
   - Use appropriate assertion methods:
     * assertLogMessagePresent
     * assertNoLogMessagePresent
     * assertSingleLogMessagePresent

3. Test Data:
   - Use LogRecord#resolveIdentifierString for message verification
   - Test both successful and error scenarios
   - Verify correct log level usage
