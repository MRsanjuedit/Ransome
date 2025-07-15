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

# === Encrypt All Files Except Skipped Ones ===
def encrypt_files(folder_path, fernet):
    for filename in os.listdir(folder_path):
        if filename in SKIP_FILES:
            continue

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as file:
                    data = file.read()

                encrypted_data = fernet.encrypt(data)

                with open(file_path, "wb") as file:
                    file.write(encrypted_data)

                print(f"[+] Encrypted: {filename}")
            except Exception as e:
                print(f"[!] Failed to encrypt {filename}: {e}")

# === MAIN ===
if __name__ == "__main__":
    key = load_or_generate_key(KEY_FILE)
    fernet = Fernet(key)

    encrypt_files(FOLDER_PATH, fernet)
    print("\n✅ Encryption complete. All files encrypted (except skipped ones).")
