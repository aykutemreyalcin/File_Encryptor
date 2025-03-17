# File Encryptor

This is a simple file encryption and decryption tool using Python's `cryptography` library.

## Features

- Generate a secret key for encryption and decryption.
- Encrypt files using the generated key.
- Decrypt files using the generated key.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:

    ```sh
    pip install cryptography
    ```

## Usage

1. **Generate a Key:**

    Run the script and choose the option to generate a key. The key will be saved as `secret.key`.

    ```sh
    python main.py
    ```

    Choose `G` to generate a key.

2. **Encrypt a File:**

    Run the script and choose the option to encrypt a file. Provide the filename you want to encrypt.

    ```sh
    python main.py
    ```

    Choose `E` to encrypt a file and enter the filename.

3. **Decrypt a File:**

    Run the script and choose the option to decrypt a file. Provide the filename you want to decrypt.

    ```sh
    python main.py
    ```

    Choose `D` to decrypt a file and enter the filename.

## Example

```sh
python main.py
```

- Choose `G` to generate a key.
- Choose `E` to encrypt a file and enter the filename (e.g., `example.txt`).
- Choose `D` to decrypt a file and enter the filename (e.g., `example.txt.enc`).

## License

This project is not licensed. You can use it for free.