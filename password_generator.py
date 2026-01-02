# password_generator.py
# Random Password Generator for AICTE Oasis Infobyte Internship
# Author: Aditya Mishra
# Date: January 2026

import string
import random

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    """
    Generate a random password with specified characteristics.
    """
    characters = ""
    mandatory_chars = []

    if use_letters:
        characters += string.ascii_letters
        mandatory_chars.append(random.choice(string.ascii_letters))

    if use_digits:
        characters += string.digits
        mandatory_chars.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    if not characters:
        raise ValueError("No character types selected.")

    if length < len(mandatory_chars):
        raise ValueError(f"Length must be at least {len(mandatory_chars)} for selected options.")

    remaining_length = length - len(mandatory_chars)
    password_chars = mandatory_chars + [
        random.choice(characters) for _ in range(remaining_length)
    ]

    random.shuffle(password_chars)
    return "".join(password_chars)


def main():
    """
    Main function to run the password generator.
    """
    print("=" * 50)
    print("Random Password Generator")
    print("=" * 50)

    try:
        length = int(input("\nEnter password length (e.g., 8, 12, 16): "))
        if length <= 0:
            print("Error: Length must be a positive integer.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for length.")
        return

    use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
    use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    try:
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print("\n" + "=" * 50)
        print(f"Generated password: {password}")
        print("=" * 50)
        print("\nCharacter types included:")
        if use_letters:
            print("  ✓ Letters (a-z, A-Z)")
        if use_digits:
            print("  ✓ Digits (0-9)")
        if use_symbols:
            print("  ✓ Symbols (!@#$%^&*)")
    except ValueError as e:
        print(f"\nError: {e}")


def run_generator():
    """
    Run password generator with retry loop.
    """
    while True:
        main()
        if input("\nDo you want to generate another password? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for using Password Generator!")
            break


if __name__ == "__main__":
    run_generator()
