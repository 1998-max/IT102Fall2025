#!/usr/bin/env python3
# Sample script that writes to a file
# By Harel Boyenge
# 10/22/2025

# Open file for writing
hackme_file = open("hackme.txt", "w")

# Write lines to the file
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
mother = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

hackme_file.write("Name: " + name + "\n")
hackme_file.write("Favorite Color: " + color + "\n")
hackme_file.write("First Pet's Name: " + pet + "\n")
hackme_file.write("Mother's Maiden Name: " + mother + "\n")
hackme_file.write("Elementary School: " + school + "\n")

# Close the file
hackme_file.close()
