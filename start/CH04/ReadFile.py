#!/usr/bin/env python3
# Sample script that reads from a file
# By Harel Boyenge
# 10/22/2025

# Open file for reading
hackme_file = open("hackme.txt", "r")

# Read the contents of the file
content = hackme_file.read()

# Print the required header and the file contents
print("Here is someone to hack - information")
print()
print(content)

# Close the file
hackme_file.close()