# AesBridge

![NPM Version](https://img.shields.io/npm/v/aes-bridge.svg)
![PyPI Version](https://img.shields.io/pypi/v/aes-bridge.svg)
![Packagist Version](https://img.shields.io/packagist/v/mervick/aes-bridge.svg)  
![CI Status](https://github.com/mervick/aes-bridge/actions/workflows/cross-test.yml/badge.svg)


**AesBridge** is a modern, secure and cross-language AES encryption library that supports **CBC**, **GCM**, and **Legacy CBC** modes.
The goal is to ensure secure, interoperable encryption across multiple platforms and programming languages.

It is the spiritual successor of the [AES Everywhere](https://github.com/mervick/aes-everywhere-legacy) project, with updated cryptography standards and cleaner APIs.

## Features

* 🛡️ **AES-256 encryption**
* 🔐 **CBC** and **GCM** modes
* 🧪 Optional **Legacy CBC** mode (OpenSSL-compatible, with salt header)
* 🌍 Unified cross-language compatibility
* ✨ Minimal and secure design
* ✅ Tested compatibility between implementations


## Implementations

* **JavaScript**: [AesBridge JS](https://github.com/mervick/aes-bridge-js)
* **PHP**: [AesBridge PHP](https://github.com/mervick/aes-bridge-php)
* **Python**: [AesBridge Python](https://github.com/mervick/aes-bridge-python)


Each implementation provides an equivalent API interface that includes the same core methods: `encrypt_cbc`, `decrypt_cbc`, `encrypt_gcm`, `decrypt_gcm`, `encrypt_legacy`, and `decrypt_legacy`.  
The method names and functionality are consistent across languages, while the actual API structure follows the conventions of each language.

## Compatibility

AesBridge is **interoperable** between all supported languages. You can encrypt data in one language and decrypt in another, as long as the same mode and passphrases are used.

## Documentation

Each implementation contains its own README with usage examples.
For general concepts, check the tests in each repository for cross-language validation.

## Tests

All implementations include unit tests, and cross-language integration tests are planned in the main repo.

## License

MIT License © 2025 [Andrey Izman](https://github.com/mervick)

