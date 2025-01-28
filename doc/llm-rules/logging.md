1. I prefer using CuiLogger for logging with 'LOGGER' as a constant name
2. I do not prefer using log4j
3. I do not prefer using slf4j
4. Log-Statements at the levels 'INFO', 'WARN', 'ERROR', 'FATAL' must be covered with unit-tests
5. I prefer the usage of 'de.cuioss.tools.logging.LogRecord' and 'de.cuioss.tools.logging.LogRecordModel' for logging using templates. For example, see https://github.com/cuioss/cui-portal-core/blob/main/modules/authentication/portal-authentication-token/src/main/java/de/cuioss/portal/authentication/token/LogMessages.java. Hints for usage:
- The API fo 'LogRecord' can be found here: https://github.com/cuioss/cui-java-tools/tree/master/src/main/java/de/cuioss/tools/logging
- Use 'LogRecord#format' for the parameterized creation of the Log-Message
- Within LogAsserts, especially on the contains-variants, use the 'LogRecord#resolveIdentifierString()' method. This usually suffices.
6. I prefer using https://github.com/cuioss/cui-test-juli-logger for testing logging aspects, especially the 'de.cuioss.test.juli.LogAsserts'
7. Hints for the CuiLogger API:
- In case of exceptions, the Exception or Throwable is always the first parameter, prior to the format String
- I prefer '%s' for string substitutions
8. Hints for 'de.cuioss.test.juli.LogAsserts':
- The first argument is the log-level, concrete 'de.cuioss.test.juli.TestLogLevel'
- Only the method 'assertNoLogMessagePresent(TestLogLevel logLevel, Class<?> logger)' needs a Logger as a parameter. All others do not need a Logger as a parameter.
