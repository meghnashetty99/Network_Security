# Playfair-Cipher
"""
This repository contains an implementation of the **Monoalphabetic Cipher** that generates a random substitution key every time it runs. It is a simple but effective encryption method where each letter in the plaintext is replaced with a randomly shuffled version of the alphabet.

## Features
- ✅Generates a Playfair Cipher 5x5 matrix based on a keyword.
- ✅Encrypts plaintext using the Playfair Cipher method.
- ✅Decrypts ciphertext back to the original plaintext
- ✅Handles duplicate letters and spaces efficiently.

## Usage

## Encryption
- The plaintext is converted to uppercase, and the letter 'J' is replaced with 'I'.
- The text is split into pairs, adding 'X' if necessary to avoid duplicate letter pairs.
- The Playfair matrix is used to encrypt the pairs based on the Playfair Cipher rules.

## Decryption
- The ciphertext is split into pairs.
- The Playfair matrix is used to decrypt the pairs based on the Playfair Cipher rules.

