import os
from cryptography.fernet import Fernet

# === CONFIGURATION ===
FOLDER_PATH = "."  # Current directory
KEY_FILE = "secret.key"
SKIP_FILES = {KEY_FILE, "encrypt.py", "decrypt.py"}

# === Load Encryption Key ===
def load_key(key_file):
    if not os.path.exists(key_file):
        raise FileNotFoundError(f"Key file '{key_file}' not found.")

    with open(key_file, "rb") as f:
        return f.read()

# === Decrypt All Files Except Skipped Ones ===
def decrypt_files(folder_path, fernet):
    for filename in os.listdir(folder_path):
        if filename in SKIP_FILES:
            continue

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()

                decrypted_data = fernet.decrypt(encrypted_data)

                with open(file_path, "wb") as file:
                    file.write(decrypted_data)

                print(f"[+] Decrypted: {filename}")
            except Exception as e:
                print(f"[!] Failed to decrypt {filename}: {e}")

# === MAIN ===
if __name__ == "__main__":
    try:
        key = load_key(KEY_FILE)
        fernet = Fernet(key)

        decrypt_files(FOLDER_PATH, fernet)
        print("\n✅ Decryption complete. All files decrypted (except skipped ones).")
    except Exception as err:
        print(f"[X] Error: {err}")
