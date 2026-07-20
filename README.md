# Scheme Interpreter

A high-performance Scheme interpreter implementation in Python, designed for flexibility and robustness.

## Overview

The Scheme interpreter is a Python-based implementation of the Scheme programming language. It aims to provide a robust and flexible solution for executing Scheme code, making it an ideal choice for developers and researchers who need a reliable Scheme interpreter. With its modular design and extensive feature set, the Scheme interpreter is well-suited for a wide range of applications, from education to research and development.

## Features

- **High-Performance Execution**: Fast and efficient execution of Scheme code, making it ideal for large-scale applications.
- **Modular Design**: Easy-to-use and modular architecture, making it simple to extend and customize the interpreter.
- **Robust Error Handling**: Comprehensive error handling and debugging features, ensuring smooth execution and reliable results.
- **Flexible Input/Output**: Support for various input/output formats, including files, strings, and interactive consoles.
- **Extensive Library Support**: Seamless integration with popular Python libraries, such as NumPy and Pandas.
- **Cross-Platform Compatibility**: Compatible with multiple operating systems, including Windows, macOS, and Linux.
- **Well-Documented Code**: Clear and concise documentation, making it easy to understand and extend the interpreter.
- **Active Community**: Engaged community of developers and researchers contributing to the project and providing support.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/tonybalbinot/scheme-interpreter.git

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the interpreter
python src/main.py

# Execute a Scheme program
(load "example.scm")

# Evaluate an expression
(+ 2 3)
```

## Architecture

The Scheme interpreter is designed with a modular architecture, consisting of the following key components:

- **Tokenizer**: Responsible for breaking down Scheme code into individual tokens.
- **Parser**: Analyzes the tokens and generates an abstract syntax tree (AST).
- **Evaluator**: Executes the AST, producing the final output.
- **Output Handler**: Formats the output according to the specified format.

Key files and their roles:

- `src/tokenizer.py`: Tokenizer implementation.
- `src/parser.py`: Parser implementation.
- `src/evaluator.py`: Evaluator implementation.
- `src/main.py`: Entry point and command-line interface.

## API Reference

The Scheme interpreter provides a clean and simple API for interacting with the interpreter. Key functions include:

- `load`: Loads a Scheme program from a file.
- `eval`: Evaluates a Scheme expression.
- `run`: Runs a Scheme program.

## Testing

```bash
# Run tests
python -m unittest discover -s tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push and open a PR

## License

MIT License
