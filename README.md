# AesBridge

[![NPM Version](https://img.shields.io/npm/v/aes-bridge.svg)](https://www.npmjs.com/package/aes-bridge)
[![PyPI Version](https://img.shields.io/pypi/v/aes-bridge.svg)](https://pypi.org/project/aes-bridge/)
[![Gem Version](https://img.shields.io/gem/v/aes-bridge.svg)](https://rubygems.org/gems/aes-bridge/versions/2.0.0)
[![NuGet Version](https://img.shields.io/nuget/v/AesBridge.svg)](https://www.nuget.org/packages/AesBridge)
[![Packagist Version](https://img.shields.io/packagist/v/mervick/aes-bridge.svg)](https://packagist.org/packages/mervick/aes-bridge)
[![Maven Central](https://img.shields.io/maven-central/v/dev.mervick.aesbridge/aes-bridge.svg)](https://central.sonatype.com/artifact/dev.mervick.aesbridge/aes-bridge)  
[![CI Status](https://github.com/mervick/aes-bridge/actions/workflows/cross-test.yml/badge.svg)](https://github.com/mervick/aes-bridge/actions/workflows/cross-test.yml)


**AesBridge** is a modern, secure and cross-language AES encryption library that supports **CBC**, **GCM**, and **Legacy CBC** modes.
The goal is to ensure secure, interoperable encryption across multiple platforms and programming languages.

It is the spiritual successor of the [AES Everywhere](https://github.com/mervick/aes-everywhere-legacy) project, with updated cryptography standards and cleaner APIs.

## Features

- **🛡️ AES-256 encryption** - Industry-standard 256-bit encryption
- **🔐 Multiple modes** - **GCM** and **CBC** with HMAC
- **🔄 Legacy CBC** - For backward compatibility with projects using **AES Everywhere**.
- **🌍 Cross-language compatibility** - Unified implementation across languages
- **✨ Secure by design** - Proper key derivation and cryptographic best practices
- **✅ Tested interoperability** - Verified compatibility between all implementations


## Implementations

* **C++**: [AesBridge CPP](https://github.com/mervick/aes-bridge-cpp)
* **C# (.NET)**: [AesBridge .NET](https://github.com/mervick/aes-bridge-dotnet)
* **GO**: [AesBridge GO](https://github.com/mervick/aes-bridge-go)
* **Java**: [AesBridge Java](https://github.com/mervick/aes-bridge-java)
* **JavaScript**: [AesBridge JS](https://github.com/mervick/aes-bridge-js)
* **PHP**: [AesBridge PHP](https://github.com/mervick/aes-bridge-php)
* **Python**: [AesBridge Python](https://github.com/mervick/aes-bridge-python)
* **Ruby**: [AesBridge Ruby](https://github.com/mervick/aes-bridge-ruby)


## Encryption Modes

The following table compares the different encryption modes available in **AesBridge**, including their cryptographic primitives, key derivation, and output formats.

| Mode           | Cipher      | Hash Algo      | KDF             | Iterations | Output Structure                             | Authentication          |
|----------------|-------------|----------------|-----------------|------------|----------------------------------------------|-------------------------|
| **GCM**        | AES-256-GCM | SHA256         | PBKDF2          | 100,000    | salt(16) + nonce(12) + ciphertext + tag(16)  | GCM Tag (16 bytes)      |
| **CBC**        | AES-256-CBC | SHA256         | PBKDF2          | 100,000    | salt(16) + iv(16) + ciphertext + hmac(32)    | HMAC-SHA256 (32 bytes)  |
| **Legacy CBC** | AES-256-CBC | MD5            | Iterative MD5   | N/A        | 'Salted__' + salt(8) + ciphertext            | None                    |


#### Notes on the Table:
- **Mode**: The encryption mode used.
- **Cipher**: The underlying AES variant.
- **Hash Algo**: The hash function used in key derivation or authentication.
- **KDF**: Key Derivation Function.
- **Iterations**: Number of iterations for key derivation (N/A for legacy mode as it uses a custom iterative MD5 approach).
- **Output Structure**: The binary format of the encrypted data (before optional base64 encoding). Note that in legacy mode, the IV is derived and not explicitly stored in the output.
- **Authentication**: Mechanism for integrity and authenticity checking. Legacy mode lacks authentication, making it vulnerable to tampering.


### Mode Details

This comparison highlights the security improvements in modern modes (GCM and CBC) over the legacy mode, which is provided for compatibility purposes only. It is recommended to use GCM or CBC for new applications.

- **AES-256-GCM:** A modern mode providing both encryption and built-in authentication via a tag for integrity checks. It supports associated data (non-encrypted but authenticated metadata) and offers high performance through parallelization. Best for new projects requiring maximum security and efficiency.

- **AES-256-CBC with HMAC:** A proven mode for block encryption, enhanced with HMAC for authentication and integrity. It uses a secure Encrypt-then-MAC approach to verify data authenticity. Suitable for applications needing reliable encryption with explicit integrity verification.

- **Legacy CBC** (backward compatibility): Replicates the behavior of older libraries like AES Everywhere for decrypting legacy data. It lacks built-in authentication, making it **less secure**; use only for compatibility, not new encryption.


## API Methods

Each implementation provides equivalent core methods with consistent behavior across languages. Method naming follows each language's conventions while maintaining functional parity.

| **Base name**        | **Mode**      | **Format** | **Description** |
|----------------------|---------------|------------|----------------|
| `encrypt_gcm()`      | GCM           | Base64     | Encrypt with GCM, return Base64-encoded |
| `decrypt_gcm()`      | GCM           | Base64     | Decrypt GCM Base64-encoded data |
| `encrypt_gcm_bin()`  | GCM           | Binary     | Encrypt with GCM, return binary |
| `decrypt_gcm_bin()`  | GCM           | Binary     | Decrypt GCM binary data |
| `encrypt_cbc()`      | CBC           | Base64     | Encrypt with CBC, return Base64-encoded |
| `decrypt_cbc()`      | CBC           | Base64     | Decrypt CBC Base64-encoded data |
| `encrypt_cbc_bin()`  | CBC           | Binary     | Encrypt with CBC, return binary |
| `decrypt_cbc_bin()`  | CBC           | Binary     | Decrypt CBC binary data |
| `encrypt_legacy()`   | Legacy CBC    | Base64     | Encrypt with AES Everywhere legacy format, return Base64-encoded |
| `decrypt_legacy()`   | Legacy CBC    | Base64     | Decrypt with AES Everywhere legacy format, decrypts Base64-encoded data |


**Base name** in the table shows the core functionality in **snake_case** format, but actual implementations follow language-specific conventions, for example:
- **C#**: `AesBridge.Gcm.EncryptBin()`
- **Go**: `aesbridge.EncryptGCMBin()`
- **Java**: `AesBridge.GCM.encryptBin()`
- **JavaScript**: `encryptGcmBin()`
- **PHP**: `AesBridge\Gcm::encryptBin()`
- **Python**: `encrypt_gcm_bin()`
- **Ruby**: `AesBridge.encrypt_gcm_bin()`

Each implementation contains its own README with exact syntax and usage examples.  


## Cross-Language Compatibility

All **AesBridge** implementations guarantee:

- **Identical cryptographic behavior** across all implementations
- **Same parameter order** (data, passphrase)
- **Identical output formats** (binary structure or Base64 encoding)
- **Matching API structure** (following language conventions)
- **Interoperable encrypted data** - encrypt in one language, decrypt in another

## **Testing & Compatibility**

Each language repository includes comprehensive **automated CI tests** that verify:

- Correct encryption/decryption for all supported modes (GCM, CBC, Legacy CBC)
- Proper handling of both string and binary data inputs
- Consistent output formats across all implementations

To ensure **perfect interoperability**, all implementations share:

- **Identical test data** (plaintexts and passphrases)
- **Pre-generated encrypted samples** for all modes:

The **main repository** includes **automated CI tests** that verify interoperability across all implementations by **Round-Trip Encryption/Decryption**:

- Encrypts test data in **each language**  
- Decrypts it in **every other supported language**  
- Validates that the output matches the original input  


This rigorous testing ensures **bit-for-bit compatibility** across all supported platforms.
