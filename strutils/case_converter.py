"""String case conversion functions (snake_case, camelCase, PascalCase).

This module provides utility functions for converting strings between
common naming conventions used in programming, including snake_case,
camelCase, and PascalCase (also known as UpperCamelCase).

Typical usage example:

    from strutils.case_converter import to_snake_case, to_camel_case, to_pascal_case

    snake = to_snake_case("myVariableName")   # "my_variable_name"
    camel = to_camel_case("my_variable_name") # "myVariableName"
    pascal = to_pascal_case("my_variable_name") # "MyVariableName"
"""
