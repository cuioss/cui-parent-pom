1. Use CuiLogger with constant name 'LOGGER'
2. Never use log4j or slf4j
3. Test coverage required for INFO/WARN/ERROR/FATAL logs
4. Use de.cuioss.tools.logging.LogRecord for template logging
5. Use cui-test-juli-logger for testing
6. Exception parameter always comes first in log methods
7. Use '%s' for string substitutions

Implementation Notes:
- LogRecord API: https://github.com/cuioss/cui-java-tools/tree/master/src/main/java/de/cuioss/tools/logging
- Use LogRecord#format for parameterized log messages
- For LogAsserts testing, use LogRecord#resolveIdentifierString()
- Use de.cuioss.test.juli.TestLogLevel for log levels in tests
