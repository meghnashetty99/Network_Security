# Elliptic Curve Cryptography (ECC) Key Exchange

## Introduction

This program implements **Elliptic Curve Cryptography (ECC) Key Exchange**, which provides a secure method for key agreement using elliptic curve arithmetic. The implementation uses the **brainpoolP256r1** curve.

## Working

- **Key Generation**:
  - Generates a **private key** (`privKey`).
  - Computes the corresponding **public key** (`pubKey`).
- **Encryption Key Calculation**:
  - Generates a **random private key** for encryption.
  - Computes a **ciphertext public key**.
  - Derives a **shared encryption key**.
- **Decryption Key Calculation**:
  - Uses the original private key to compute the **decryption key**.
- **Key Verification**:
  - Checks if the **encryption key** and **decryption key** match.

## `compress_point(point)`

Compresses an elliptic curve point to a compact hex format.

## `ecc_calc_encryption_key(pubKey)`

Generates a **shared ECC key** and a **ciphertext public key**.

## `ecc_calc_decryption_key(privKey, ciphertextPubKey)`

Computes the **decryption key** using the private key.

## Example Output
![Image](https://github.com/user-attachments/assets/f49d36d9-ccf5-409f-a96a-045a2cfa7e6c)

