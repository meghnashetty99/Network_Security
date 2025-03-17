# Diffie-Hellman Key Exchange Implementation

## Introduction

This program implements the **Diffie-Hellman Key Exchange** algorithm, which is used for secure key exchange over an insecure channel. It allows two parties to generate a **shared secret key** without directly transmitting it.

## Working

- Choose a **prime number (q)** and a **primitive root (a)**.
- Select **private keys (Xa, Xb)** for users **A** and **B**.
- Compute **public keys (Ya, Yb)** using:
  Ya = (a^Xa) % q Yb = (a^Xb) % q
- Exchange public keys and compute the **shared secret key**:
  Ka = (Yb^Xa) % q Kb = (Ya^Xb) % q
- Both parties end up with the same shared key.

## Example Output
![Image](https://github.com/user-attachments/assets/b1e21b8c-6404-4259-9281-01ce688e8265)





