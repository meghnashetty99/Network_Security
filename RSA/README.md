# RSA Algorithm Implementation

## Introduction

This program implements the **RSA encryption and decryption algorithm** using two prime numbers. RSA is an **asymmetric cryptographic algorithm** that uses **public and private keys** for secure communication.

## Working

- **Choose two prime numbers (p, q)**.
- Compute **n = p × q**.
- Compute **Euler's Totient Function (φ(n)) = (p - 1) × (q - 1)**.
- Find **public key exponent (e)** such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
- Compute **private key exponent (d)** such that `(d × e) % φ(n) = 1`.
- Encrypt the message using `c = (msg^e) % n`.
- Decrypt the message using `d = (c^d) % n`.

## `gcd(a, b)`

Finds the **greatest common divisor (GCD)** of two numbers.

## `RSA(p, q, msg)`

- Generates **public and private keys**.
- Encrypts the input message.
- Decrypts the encrypted message.

## Example Output


