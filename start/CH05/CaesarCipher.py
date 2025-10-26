#!/usr/bin/env python3
# Script that encrypts/decrypts text using the Caesar Cipher
# By David Tshibamba
# Date: 10/26/2025

# Prompt for the source message
source_message = input("Enter a message: ")

# Prompt for shift value
shift = int(input("Enter the shift value (1-25): "))

# Create an empty string to store the final message
final_message = ""

# Loop through each letter in the source message
for letter in source_message:
    # Convert the letter to the ASCII equivalent
    ascii_num = ord(letter)

    # Check if the character is an uppercase letter (A-Z)
    if ascii_num >= 65 and ascii_num <= 90:
        new_ascii = ((ascii_num - 65 + shift) % 26) + 65
        final_message = final_message + chr(new_ascii)

    # Check if the character is a lowercase letter (a-z)
    elif ascii_num >= 97 and ascii_num <= 122:
        new_ascii = ((ascii_num - 97 + shift) % 26) + 97
        final_message = final_message + chr(new_ascii)

    # If not a letter, leave it unchanged
    else:
        final_message = final_message + letter

# Print the encrypted message
print("Encrypted message:")
print(final_message)

# Ask the user if they want to decrypt the message
choice = input("Decrypt the message? (yes/no): ").lower()

if choice == "yes":
    decrypted_message = ""

    # Loop through each letter of the encrypted message
    for letter in final_message:
        ascii_num = ord(letter)

        # Reverse the encryption shift for uppercase letters
        if ascii_num >= 65 and ascii_num <= 90:
            new_ascii = ((ascii_num - 65 - shift) % 26) + 65
            decrypted_message = decrypted_message + chr(new_ascii)

        # Reverse the encryption shift for lowercase letters
        elif ascii_num >= 97 and ascii_num <= 122:
            new_ascii = ((ascii_num - 97 - shift) % 26) + 97
            decrypted_message = decrypted_message + chr(new_ascii)

        else:
            decrypted_message = decrypted_message + letter

    # Print the decrypted message
    print("Decrypted message:")
    print(decrypted_message)
else:
    print("Decryption skipped.")
