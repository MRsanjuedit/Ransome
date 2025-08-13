# Rannsomeware- MINI

A Python-based utility to **encrypt and decrypt files** in a folder and all its subfolders using **Fernet symmetric encryption** from the `cryptography` library. 

This tool is intended for **educational purposes only** to learn about file encryption and decryption safely.

---

## Features

- Encrypt all files in a folder and its subfolders recursively.
- Decrypt previously encrypted files using the same key.
- Automatically generates a Fernet key if one does not exist.
- Skips specified files to prevent encrypting scripts or key files.
- Provides clear logging for encrypted, decrypted, and skipped files.

---

## ⚠️ Warning

- **Do not run this on important files** without backups.
- Losing the encryption key (`secret.key`) will make it impossible to decrypt files.
- This tool is for **learning purposes** only and should **not be used as ransomware**.

---

## Configuration

```python
FOLDER_PATH = "."  # Folder to encrypt/decrypt
KEY_FILE = "secret.key"  # Encryption key file
SKIP_FILES = {KEY_FILE, "encrypt.py", "decrypt.py"}  # Files to skip
```

- `FOLDER_PATH`: Path to the folder you want to encrypt/decrypt.
- `KEY_FILE`: Path to the file that stores the encryption key.
- `SKIP_FILES`: Files that should never be encrypted or decrypted.

---

## Usage

### Encrypt Files

```bash
python encrypt.py
```

- Encrypts all files in the specified folder and subfolders, except skipped files.
- If the key file does not exist, it will be generated automatically.

### Decrypt Files

```bash
python decrypt.py
```

- Decrypts all files that were previously encrypted using the same key.
- Skipped files remain unchanged.

---

## Dependencies

- Python 3.8+
- [cryptography](https://pypi.org/project/cryptography/)

Install dependencies using:

```bash
pip install cryptography
```

---

## Project Structure

```
.
├── encrypt.py      # Script to encrypt files
├── decrypt.py      # Script to decrypt files
├── secret.key      # Encryption key (auto-generated)
└── README.md       # Project documentation
```

---

## License

This project is for **educational purposes**. Use responsibly.
