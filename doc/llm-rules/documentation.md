1. Only document existing code elements - no speculative or planned features
2. All references must be verified to exist
3. Use linking instead of duplication
4. Code examples must come from actual unit tests
5. All javadoc changes require successful javadoc build with zero errors/warnings
6. Use consistent terminology:
   - Always use "Java beans" instead of "Jakarta beans"
   - Maintain "Java Bean Specification" terminology
   - This applies to all documentation (Javadoc, code comments, README files)
7. Code examples must follow these rules:
   - Must be complete and compilable
   - Include all necessary imports
   - Show proper error handling
   - Follow project coding standards
   - Be verified by unit tests
   - Structure:
     * Start with setup/configuration
     * Show main functionality
     * Include error handling
     * Demonstrate cleanup if needed

Package Documentation Structure:
1. Overview section explaining purpose and scope
2. Key Components section listing main classes/interfaces
3. Usage Examples with actual code samples
4. Best Practices section with guidelines
5. Cross-references to related components
6. Author and version information

Class/Interface Documentation:
1. Clear purpose description
2. Parameter descriptions with validation rules
3. Return value descriptions
4. Exception documentation
5. Usage examples from unit tests
6. Version information with @since tags
7. Thread-safety notes where applicable

Method Documentation:
1. Precise description of functionality
2. Parameter validation rules
3. Return value guarantees
4. Exception conditions
5. Thread-safety notes where applicable