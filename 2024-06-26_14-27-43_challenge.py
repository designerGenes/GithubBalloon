"""
Challenge:
Write a Python program that generates a random password of a specified length for a user. 
The password should include a mix of uppercase letters, lowercase letters, numbers, and special characters. 
The user should be able to specify the length of the password when running the program. 
The program should then generate a random password of the specified length and display it to the user. 
The password should include at least one uppercase letter, one lowercase letter, one number, and one special character.

My solution:
"""

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(numbers),
                random.choice(special_characters)]
    
    remaining_length = length - 4
    
    for _ in range(remaining_length):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    
    random.shuffle(password)
    
    return "".join(password)

# Get user input for the length of the password
password_length = int(input("Enter the length of the password: "))

# Generate and display the random password
print(f"Random password of length {password_length}: {generate_password(password_length)}")