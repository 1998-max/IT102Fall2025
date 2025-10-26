#!/usr/bin/env python3
# Script that encrypts/decrypts text using AES-128 in CBC mode
# By Harel Boyenge
# date: 10/26/2025


import os
from base64 import b64encode  # (kept simple; decode to str not required for the assignment)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


# Generate a random AES key (16 bytes for AES-128)
key = os.urandom(16)
print(f"Generated AES Key: {key!r}")

# Prompt user for plaintext input
plaintext = input("Enter a plaintext message: ")

# Pad the plaintext to a multiple of 16 bytes (AES block size = 128 bits)
padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plaintext.encode("utf-8")) + padder.finalize()

# Generate a random initialization vector (IV) - 16 bytes
iv = os.urandom(16)

# Encrypt the plaintext (AES-CBC)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# Display the encrypted message in base64 for readability
# (Printing the bytes form to match the example style with b'...'):
print(f"Encrypted message: {b64encode(ciphertext)!r}")

# Decrypt the ciphertext (using the same key and IV)
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# Remove PKCS7 padding
unpadder = padding.PKCS7(128).unpadder()
decrypted_message = unpadder.update(decrypted_padded) + unpadder.finalize()

# Display the decrypted message
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
