"""strutils - A collection of string utility functions for Python.

This package provides utilities for string manipulation including:
- Case conversion (snake_case, camelCase, PascalCase)
- String validation utilities

Example:
    >>> from strutils import to_snake_case, is_valid_identifier
    >>> to_snake_case("HelloWorld")
    'hello_world'
    >>> is_valid_identifier("valid_name")
    True
"""

__version__ = "0.1.0"
__author__ = "Ultron Creator Agent"
__all__ = [
    # Version info
    "__version__",
    # Case conversion functions (to be imported from case_converter module)
    # "to_snake_case",
    # "to_camel_case",
    # "to_pascal_case",
    # Validation functions (to be imported from validators module)
    # "is_valid_identifier",
    # "is_valid_email",
]

# Note: Actual function imports will be added in subsequent steps
# when the case_converter and validators modules are implemented.
# This keeps the package structure clean and allows for incremental development.
