'''
Challenge: Create a Python program that takes a string as input and checks if the characters form a palindrome, ignoring any non-alphabetic characters. The program should return True if the string is a palindrome and False otherwise.

My solution:
'''

def is_palindrome(input_string):
    clean_string = ''.join(char for char in input_string if char.isalpha()).lower()
    return clean_string == clean_string[::-1]

# Test the function with an example
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))  # Output: True