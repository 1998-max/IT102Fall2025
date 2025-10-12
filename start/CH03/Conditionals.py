#!/usr/bin/env python3
# Example working with conditionals
# By Dillon

# First we have to gather if the day is good or bad, which requires user input
question = input("Is today a good day? Please answer with y or n: ").lower()

# Analyze the value and print if yes it is
if question == 'y':
    print("Yes it is")
elif question == 'n':
    print("That's okay, tomorrow will be")
elif question == 'idk':
    print("That's okay")
else:
    print("Please enter a valid input of y or n for yes or no")