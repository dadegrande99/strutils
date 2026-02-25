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

Attributes:
    __version__ (str): The current version of the strutils package.
    __author__ (str): The author of the strutils package.
    __all__ (list): The list of public symbols exported by this package.
"""

__version__ = "0.1.0"
__author__ = "Ultron Creator Agent"
__all__ = [
    # Version info exported for introspection (e.g., strutils.__version__)
    "__version__",
    # Case conversion functions (to be imported from case_converter module)
    # Uncomment each entry below once the corresponding module is implemented:
    # "to_snake_case",   # Converts CamelCase or mixed strings to snake_case
    # "to_camel_case",   # Converts snake_case or mixed strings to camelCase
    # "to_pascal_case",  # Converts snake_case or mixed strings to PascalCase
    # Validation functions (to be imported from validators module)
    # Uncomment each entry below once the corresponding module is implemented:
    # "is_valid_identifier",  # Checks whether a string is a valid Python identifier
    # "is_valid_email",       # Checks whether a string is a properly formatted email address
]

# NOTE: Actual function imports will be added in subsequent steps
# when the case_converter and validators modules are implemented.
# This keeps the package structure clean and allows for incremental,
# test-driven development without breaking existing imports.
