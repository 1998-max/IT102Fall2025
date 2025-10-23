#!/usr/bin/env python3
# example workign with Functions
# By Harel Boyenge
# 10/22/2025

# Define a function that contains the looping "Yeah it is" message
def send_message():
    number = 1
    while number <= 10:
        print("Yeah it is")
        number += 1

# Ask the user for input
question = input("Is today a good day? Please answer with y or n: ").lower()

# Analyze the input and use the function when appropriate
if question == 'y':
    send_message()  
elif question == 'n':
    print("That's okay, tomorrow will be")
elif question == 'idk':
    print("That's okay")
else:
    print("Please enter a valid input of y or n for yes or no")
