# AesBridge

**AesBridge** is a modern, secure and cross-language AES encryption library that supports **CBC**, **GCM**, and **Legacy CBC** modes.
The goal is to ensure secure, interoperable encryption across multiple platforms and programming languages.

It is the spiritual successor of the [AES Everywhere](https://github.com/mervick/aes-everywhere-legacy) project, with updated cryptography standards and cleaner APIs.

## 🔐 Features

* AES-256 encryption
* CBC and GCM modes
* Optional Legacy CBC mode (OpenSSL-compatible, with salt header)
* Cross-language compatibility
* Minimal and secure design
* Tested compatibility between implementations

## 📦 Implementations

* **PHP**: [https://github.com/mervick/aes-bridge-php](https://github.com/mervick/aes-bridge-php) (AesBridge PHP)
* **Python**: [https://github.com/mervick/aes-bridge-python](https://github.com/mervick/aes-bridge-python) (AesBridge Python)
* **JavaScript**: [https://github.com/mervick/aes-bridge-js](https://github.com/mervick/aes-bridge-js) (AesBridge JS)

Each implementation provides the same API interface: `encrypt_cbc`, `decrypt_cbc`, `encrypt_gcm`, `decrypt_gcm`, `encrypt_legacy`, and `decrypt_legacy`.

## 🔄 Compatibility

AesBridge is **interoperable** between all supported languages. You can encrypt data in one language and decrypt in another, as long as the same algorithm and keys are used.

## 📚 Documentation

Each implementation contains its own README with usage examples.
For general concepts, check the tests in each repository for cross-language validation.

## 🧪 Tests

All implementations include unit tests, and cross-language integration tests are planned in the main repo.

## 📜 License

MIT License © 2025 [Andrey Izman](https://github.com/mervick)

