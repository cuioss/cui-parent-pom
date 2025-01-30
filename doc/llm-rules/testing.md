# Testing Framework Guidelines

## Core Testing Principles

### Test Structure
1. Follow AAA pattern (Arrange-Act-Assert)
2. One logical assertion per test
3. Clear test naming convention
4. Descriptive test documentation

### Test Coverage Requirements
1. Minimum 80% line coverage
2. Critical paths must have 100% coverage
3. All public APIs must be tested
4. Edge cases must be covered

## Testing Tools

### Required Frameworks
1. JUnit 5
   - Use `@DisplayName` for readable test names
   - Leverage parameterized tests
   - Apply proper test lifecycle annotations

### CUI Testing Utilities
1. cui-test-generator
   - Use for generating test data
   - Follow builder patterns
   - Document generator configurations

2. cui-test-value-objects
   - Leverage for value object testing
   - Follow equality testing guidelines
   - Include serialization tests

3. cui-jsf-test-basic
   - Use for JSF component testing
   - Follow component test patterns
   - Include lifecycle tests

## Test Categories

### Unit Tests
1. Test single units in isolation
2. Mock all dependencies
3. Fast execution
4. High maintainability

### Integration Tests
1. Test component interactions
2. Minimal mocking
3. Cover critical paths
4. Include error scenarios

### System Tests
1. End-to-end scenarios
2. Real dependencies where possible
3. Cover main user flows
4. Include performance criteria

## Best Practices

1. Test Independence
   - No test dependencies
   - Clean test environment
   - Predictable test data

2. Test Maintainability
   - DRY in test utilities
   - Clear test documentation
   - Consistent patterns

3. Test Performance
   - Fast test execution
   - Efficient resource usage
   - Parallel test execution where possible

4. Test Quality
   - Regular test review
   - Mutation testing
   - Test failure analysis