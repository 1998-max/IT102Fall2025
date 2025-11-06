#!/usr/bin/env python3
# Script that Genarate password
#By Harel Boyenge


import secrets
import string

def prompt_yes_no(prompt):
    while True:
        r = input(f"{prompt} (y/n): ").strip().lower()
        if r in ("y","yes"):
            return True
        if r in ("n","no"):
            return False
        print("Please answer 'y' or 'n'.")

def get_int_input(prompt, default=12):
    s = input(f"{prompt} (default {default}): ").strip()
    if s == "":
        return default
    if s.isdigit():
        return int(s)
    print("Invalid number, using default.")
    return default

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Build pool
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    if not pool:
        # fallback to lowercase
        pool = string.ascii_lowercase
        use_lower = True

    # Ensure at least one char of each chosen class
    chars = []
    if use_upper:
        chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        chars.append(secrets.choice(string.digits))
    if use_special:
        chars.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"))

    # Fill the rest from pool
    while len(chars) < length:
        chars.append(secrets.choice(pool))

    # Shuffle chars securely
    for i in range(len(chars)-1, 0, -1):
        j = secrets.randbelow(i+1)
        chars[i], chars[j] = chars[j], chars[i]

    return "".join(chars)

def main():
    print("Secure password generator (minimum length 8).")
    while True:
        length = get_int_input("Enter desired password length (>=8)", default=12)
        if length < 8:
            print("Length must be at least 8. Setting to 8.")
            length = 8

        use_upper = prompt_yes_no("Include uppercase letters (A-Z)?")
        use_lower = prompt_yes_no("Include lowercase letters (a-z)?")
        use_digits = prompt_yes_no("Include numbers (0-9)?")
        use_special = prompt_yes_no("Include special characters (e.g. !@#$)?")

        if not (use_upper or use_lower or use_digits or use_special):
            print("No character groups selected; defaulting to lowercase + digits.")
            use_lower = True
            use_digits = True

        pwd = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("\nGenerated password:\n" + pwd + "\n")

        again = prompt_yes_no("Generate another password?")
        if not again:
            print("Done. Stay secure!")
            break

if __name__ == "__main__":
    main()