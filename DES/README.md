# DES Key Generation

## Introduction

This program implements the **Key Generation** process of the **Data Encryption Standard (DES)** algorithm. It takes a **64-bit binary key** as input, applies **permutations and shifts**, and generates **16 subkeys** used in the encryption process.

## Working

- **Initial Permutation (PC1)**: Reduces the 64-bit key to 56 bits.
- **Left and Right Key Splitting**: The key is split into two 28-bit halves.
- **Left Circular Shifts**: Each half is rotated based on predefined shift values.
- **Permutation Choice 2 (PC2)**: Produces the final **48-bit subkeys**.
- **Generates 16 Subkeys**, one for each DES encryption round.

## `permute(input, table)`

Performs permutation on the input string based on the given table.

## `leftShift(input, shifts)`

Shifts the input string left by the given number of positions.

## Output Example
![Image](https://github.com/user-attachments/assets/896545ee-015b-435a-b2e3-a4b499816574)

