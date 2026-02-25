# strutils

A lightweight Python package providing utility functions for string manipulation, including case conversion and string validation helpers.

## Project Overview

`strutils` is a simple, dependency-free Python library built on top of Python's standard library (`re` and `keyword`). It offers a clean set of functions for converting strings between common naming conventions and for validating strings against common patterns.

## Features

- **Case Conversion**
  - Convert strings to `camelCase`
  - Convert strings to `snake_case`
  - Convert strings to `kebab-case`
- **String Validation**
  - Check whether a string is a valid email address
  - Check whether a string is a valid Python identifier
  - Match strings against arbitrary patterns

## Installation

**Requirements:** Python >= 3.8

Clone the repository and install the package locally:

```bash
git clone <repository-url>
cd strutils
pip install .
```

For development (includes `pytest`):

```bash
pip install -e ".[dev]"
```

## Usage

### Case Conversion

```python
from strutils import to_camel_case, to_snake_case, to_kebab_case

# Convert to camelCase
to_camel_case("hello_world")        # → "helloWorld"
to_camel_case("foo bar baz")        # → "fooBarBaz"

# Convert to snake_case
to_snake_case("helloWorld")         # → "hello_world"
to_snake_case("FooBarBaz")          # → "foo_bar_baz"

# Convert to kebab-case
to_kebab_case("helloWorld")         # → "hello-world"
to_kebab_case("foo_bar_baz")        # → "foo-bar-baz"
```

### String Validation

```python
from strutils import is_valid_email, is_valid_identifier

# Email validation
is_valid_email("user@example.com")  # → True
is_valid_email("not-an-email")      # → False

# Python identifier validation
is_valid_identifier("my_variable")  # → True
is_valid_identifier("class")        # → False  (reserved keyword)
is_valid_identifier("123abc")       # → False
```

## Development

Install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Ensure all tests pass with `pytest`.
5. Submit a pull request with a clear description of your changes.
