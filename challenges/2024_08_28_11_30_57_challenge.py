'''
Challenge: Create a Python program that generates a random password of a specified length for a user. The password should include a mix of uppercase letters, lowercase letters, numbers, and special characters. The user should be able to specify the length of the password and whether they want to include special characters or not. The program should then display the randomly generated password to the user.
'''

import random
import string

def generate_password(length, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password length and special character inclusion
password_length = int(input("Enter the length of the password: "))
include_special_chars = input("Include special characters? (yes/no): ").lower()

if include_special_chars == 'yes':
    generated_password = generate_password(password_length, True)
else:
    generated_password = generate_password(password_length, False)

print(f"Generated Password: {generated_password}")
