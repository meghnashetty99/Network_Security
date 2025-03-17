# Hill-cipher

## Features
- ✅ Encrypts messages using a given key matrix.
- ✅ Decrypts messages back to plaintext using the inverse key matrix.
- ✅ Handles padding automatically to fit the matrix size.
- ✅ Uses modular arithmetic to compute the inverse matrix.

## How It Works
- The plaintext is converted to uppercase and spaces are removed.
- The text is divided into blocks of size n, where n is the dimension of the key matrix.
- Matrix multiplication is performed to encrypt the blocks.
- The decryption process uses the modular inverse of the key matrix.

