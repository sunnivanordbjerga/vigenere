# Vigenere Encrypter / Decrypter

[![CI](https://github.com/sunnivanordbjerga/vigenere/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sunnivanordbjerga/vigenere/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/sunnivanordbjerga/vigenere/graph/badge.svg?token=KW7TELRQM5)](https://codecov.io/github/sunnivanordbjerga/vigenere)
![Python](https://img.shields.io/badge/python-3.14-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A lightweight Vigenére encryption and decryption terminal program.*

<br>

![Vigenere gif](vigenere.gif)

<br>

---
## Features
- Symmetric cryptography
- Defensive input validation

---
## Project structure
```
├── src/                  # Source code
│   ├── main.py           # Terminal CLI application entrypoint
│   └── vigenere.py       # Core cryptographic algorithms
├── tests/                # Tests
│   └── test_vigenere.py
└── pyproject.toml        # Project metadata, tools (Ruff, Pytest), and dependencies
```

---

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

---

## Authors
Sunniva Nord Bjerga

---

## License
This project is licensed under an MIT license - see [LICENSE](LICENSE)
