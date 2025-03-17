from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
    print("File encrypted successfully!")

def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully!")

if __name__ == "__main__":
    choice = input("Do you want to (G)enerate a key, (E)ncrypt a file, or (D)ecrypt a file? ").strip().upper()
    
    if choice == "G":
        generate_key()
        print("Encryption key generated and saved as 'secret.key'.")
    elif choice == "E":
        key = load_key()
        filename = input("Enter the filename to encrypt: ")
        encrypt_file(filename, key)
    elif choice == "D":
        key = load_key()
        filename = input("Enter the filename to decrypt: ")
        decrypt_file(filename, key)
    else:
        print("Invalid choice. Exiting.")