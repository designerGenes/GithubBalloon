'''
Challenge: 
Create a Python function that takes in a string and returns True if the string is a palindrome, and False otherwise.
Ignore spaces, capitalization, and punctuation when determining if the string is a palindrome.
The function should be case-insensitive and should ignore any non-alphanumeric characters.

My solution:
'''

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("race a car"))  # False