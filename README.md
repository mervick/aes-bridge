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
- **🔐 Multiple modes** - **GCM** and **CBC with HMAC**
- **↩️ Legacy CBC** - For backward compatibility with projects using **AES Everywhere**.
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

#### **1. GCM (Galois/Counter Mode) - AES 256 with Tag**

* A modern mode providing both **encryption and authentication** (integrity check).
* Generates an **authentication tag** to verify data hasn't been tampered with. Supports **Associated Data** (non-encrypted but authenticated metadata). High performance due to parallelization.
* Recommended for most **new projects** requiring maximum security and data integrity.

#### **2. CBC (Cipher Block Chaining) with HMAC Verification - AES 256**

* A time-tested mode for **encryption**, enhanced with **HMAC** for **authentication and integrity**.
* Chained block encryption. The secure "Encrypt-then-MAC" (EtM) approach is used, where **HMAC** verifies the authenticity of the encrypted data.


#### **3. CBC Legacy (for AES Everywhere backward compatibility)**

* **CBC** mode precisely mimicking the behavior of the older **AES Everywhere** library.
* Primary purpose is **backward compatibility**. Allows decryption of data encrypted with AES Everywhere, and vice-versa. Doesn't include built-in integrity checks like GCM or CBC+HMAC, as it replicates the older behavior.
* For new projects, using **GCM** or **CBC** with HMAC is recommended.

## Cross-Language Compatibility

All **AesBridge** implementations guarantee:

- **Identical cryptographic behavior** across all implementations
- **Same parameter order** (data, passphrase)
- **Identical output formats** (binary structure or Base64 encoding)
- **Matching API structure** (following language conventions)
- **Interoperable encrypted data** - encrypt in one language, decrypt in another


## API Methods

Each implementation provides equivalent core methods with consistent behavior across languages. Method naming follows each language's conventions while maintaining functional parity.

| **Functionality**          | **Mode**      | **Format** | **Base name** *      | **Description** |
|----------------------------|---------------|------------|----------------------|----------------|
| **GCM Encryption**         | GCM           | Base64     | `encrypt_gcm()`      | Encrypt with GCM, return Base64 |
| **GCM Decryption**         | GCM           | Base64     | `decrypt_gcm()`      | Decrypt GCM Base64 data |
| **GCM Binary Encryption**  | GCM           | Binary     | `encrypt_gcm_bin()`  | Encrypt with GCM, return binary |
| **GCM Binary Decryption**  | GCM           | Binary     | `decrypt_gcm_bin()`  | Decrypt GCM binary data |
| **CBC Encryption**         | CBC           | Base64     | `encrypt_cbc()`      | Encrypt with CBC, return Base64 |
| **CBC Decryption**         | CBC           | Base64     | `decrypt_cbc()`      | Decrypt CBC Base64 data |
| **CBC Binary Encryption**  | CBC           | Base64     | `encrypt_cbc_bin()`  | Encrypt with CBC, return binary |
| **CBC Binary Decryption**  | CBC           | Base64     | `decrypt_cbc_bin()`  | Decrypt CBC binary data |
| **Legacy Encryption**      | Legacy CBC    | Base64     | `encrypt_legacy()`   | AES Everywhere legacy format, return Base64 |
| **Legacy Decryption**      | Legacy CBC    | Base64     | `decrypt_legacy()`   | AES Everywhere legacy decryption (decrypts Base64 data) |

\* **Language-Specific Naming Notes:**

**Base name** shows the core functionality in **snake_case** format, but actual implementations follow language-specific conventions, for example:
- **C#**: `AesBridge.Gcm.EncryptBin()`
- **Go**: `aesbridge.EncryptGCMBin()`
- **Java**: `AesBridge.GCM.encryptBin()`
- **JavaScript**: `encryptGcmBin()`
- **PHP**: `AesBridge\Gcm::encryptBin()`
- **Python**: `encrypt_gcm_bin()`
- **Ruby**: `AesBridge.encrypt_gcm_bin()`

Each language implementation maintains its own idiomatic structure including:
- Namespace/class organization
- Case conventions (camelCase, PascalCase, snake_case)

Each implementation contains its own README with exact syntax and usage examples.  


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
