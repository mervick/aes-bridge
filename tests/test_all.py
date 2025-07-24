from typing import Literal
import unittest
import json
import subprocess
import base64
import os
import secrets

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Function to run a command and return stdout
def run_command(command_parts, cwd=None):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command_parts)}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise

class TestAesBridge(unittest.TestCase):
    pass


def add_test(name, method, *args):
    setattr(TestAesBridge, name, method(name, *args))

def to_bytes(s: str | bytes) -> bytes:
    """ Convert string to bytes. """
    return s.encode('utf-8') if isinstance(s, str) else s

def to_str(s: str | bytes):
    """ Convert bytes to string. """
    return s.decode('utf-8') if isinstance(s, bytes) else s

class CliExecutor:
    def __init__(self, language: str, path: str, executor: str, working_directory = None):
        self.language = language
        self.path = os.path.join(project_root, path) if len(path) > 0 else ""
        self.executor = executor
        self.working_directory = working_directory

    def execute(self, action: Literal["encrypt", "decrypt"], mode: Literal["gcm", "cbc", "legacy"], data: bytes | str, passphrase: bytes | str):
        data = to_bytes(data)

        if action == "encrypt":
            data = base64.b64encode(data)

        command = list(self.executor.split() +
                  ([self.path] if len(self.path) > 0 else []) +
                  [ action,
                   "--mode", mode,
                   "--data", to_str(data),
                   "--passphrase", to_str(passphrase),
                   "--b64"])
        result = run_command(command, cwd=self.working_directory)

        if action == "decrypt":
            result = base64.b64decode(result)
        return result

    def encrypt_cbc(self, data, passphrase):
        return self.execute("encrypt", "cbc", data, passphrase)

    def encrypt_gcm(self, data, passphrase):
        return self.execute("encrypt", "gcm", data, passphrase)

    def encrypt_legacy(self, data, passphrase):
        return self.execute("encrypt", "legacy", data, passphrase)

    def decrypt_cbc(self, data, passphrase):
        return self.execute("decrypt", "cbc", data, passphrase)

    def decrypt_gcm(self, data, passphrase):
        return self.execute("decrypt", "gcm", data, passphrase)

    def decrypt_legacy(self, data, passphrase):
        return self.execute("decrypt", "legacy", data, passphrase)


def load_cli_tests():
    # Load configuration
    local_config = "tests/cli_config_local.json"
    default_config = "tests/cli_config.json"
    config_path = local_config if os.path.exists(local_config) else default_config

    with open(config_path, 'r') as f:
        config = json.load(f)

    # Load test data
    with open('tests/test_data.json', 'r') as f:
        test_data = json.load(f)

    def test_encrypt_decrypt(name, encryptor, decryptor, data, passphrase):
        data = to_bytes(data)
        passphrase = to_bytes(passphrase)
        def test(self):
            # print(f"Running test: {name}")
            encrypted = encryptor(data, passphrase)
            decrypted = decryptor(encrypted, passphrase)
            self.assertEqual(data, decrypted, "Encryption/decryption failed")
        return test

    languages = list(config.keys())
    executors = {}

    passphrase = to_bytes("P@ssw0rd 😄")

    for lang in languages:
        lang_config = config[lang]
        executor = CliExecutor(lang, lang_config.get('path', ""), lang_config['executor'], lang_config.get('working_directory'))
        executors[lang] = executor

    for enc_lang in languages:
        encryptor = executors[enc_lang]

        for dec_lang in languages:
            # Skip if encryptor and decryptor are the same language
            if enc_lang == dec_lang:
                continue

            decryptor = executors[dec_lang]

            test_key = 'plaintext'
            # join all tests data
            test_text = "\n".join(test_data.get('testdata', {}).get('plaintext', []))
            # for idx, test_text in enumerate(test_data.get('testdata', {}).get('plaintext', [])):
            if len(test_text) > 0:
                add_test(f"test_cbc__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt, encryptor.encrypt_cbc, decryptor.decrypt_cbc, test_text, passphrase)
                add_test(f"test_gcm__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt, encryptor.encrypt_gcm, decryptor.decrypt_gcm, test_text, passphrase)
                add_test(f"test_legacy__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt, encryptor.encrypt_legacy, decryptor.decrypt_legacy, test_text, passphrase)

            test_key = 'hex'
            # join all tests data
            hex_text = "".join(test_data.get('testdata', {}).get('hex', []))
            # for idx, hex_text in enumerate(test_data.get('testdata', {}).get('hex', [])):
            test_text = bytes.fromhex(hex_text)
            if len(test_text) > 0:
                add_test(f"test_cbc__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt, encryptor.encrypt_cbc, decryptor.decrypt_cbc, test_text, passphrase)
                add_test(f"test_gcm__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt, encryptor.encrypt_gcm, decryptor.decrypt_gcm, test_text, passphrase)
                add_test(f"test_legacy__encrypt_{enc_lang}__decrypt_{dec_lang}__{test_key}", test_encrypt_decrypt,encryptor.encrypt_legacy, decryptor.decrypt_legacy, test_text, passphrase)

load_cli_tests()

if __name__ == '__main__':
    unittest.main()
