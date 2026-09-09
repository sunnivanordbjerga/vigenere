# Vigenere Encoder / Decoder

[![CI](https://github.com/sunnivanordbjerga/vigenere/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sunnivanordbjerga/vigenere/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/sunnivanordbjerga/vigenere/graph/badge.svg?token=KW7TELRQM5)](https://codecov.io/github/sunnivanordbjerga/vigenere)
![Python](https://img.shields.io/badge/python-3.14-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A lightweight Vigénere encryption and decryption terminal program.*

## Features
- *Symmetric cryptography*
- *Defensive input validation*

## Project structure
```
├── src/             # Source code
│   ├── main.py      # Terminal CLI application entrypoint
│   └── vigenere.py  # Core cryptographic algorithms
├── tests/           # Tests
│   └── test_vigenere.py
└── pyproject.toml   # Project metadata, tools (Ruff, Pytest), and dependencies
```
## Installation and running
### Clone
```bash
   git clone https://github.com/sunnivanordbjerga/vigenere
   cd vigenere
```
### Install dependencies
 ```bash
   pip install -e .[dev]
 ```
### Test
```bash
pytest
```
### Checking Code Coverage
Test coverage is automatically reported via `pytest-cov`
```bash
pytest --cov=src 
```
### Code Formatting & Linting
```bash
# Check for code quality issues
ruff check .

# Automatically format the code style
ruff format .
```

## License
This project is licensed under an MIT license - see [LICENSE](LICENSE)