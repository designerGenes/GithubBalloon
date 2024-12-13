'''
Challenge: 
Create a Python function that takes a string as input and returns True if the string is a palindrome, and False otherwise. Remember that a palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Your function should be case-insensitive and should ignore any non-alphanumeric characters.
'''

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
    
'''