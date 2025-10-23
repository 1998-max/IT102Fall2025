#!/usr/bin/env python3
# Sample script that writes to a file
# By Harel Boyenge

# Open the file in write mode
with open("hackme.txt", "w") as file:
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    pet = input("What was your first pet's name? ")
    mother = input("What is your mother's maiden name? ")
    school = input("What elementary school did you attend? ")

    file.write("Name: " + name + "\n")
    file.write("Favorite Color: " + color + "\n")
    file.write("First Pet's Name: " + pet + "\n")
    file.write("Mother's Maiden Name: " + mother + "\n")
    file.write("Elementary School: " + school + "\n")

# Read the file back and print the content
with open("hackme.txt", "r") as file:
    content = file.read()
    print("\nSaved Information:\n")
    print(content)