'''
Challenge: "Vowel Palindrome"

Create a function that takes in a string and returns True if the string is a palindrome and contains at least one vowel, ignoring case. Otherwise, return False. Palindromes are strings that read the same backward as forward. Vowels are defined as 'a', 'e', 'i', 'o', 'u'. The function should ignore spaces and punctuation when checking for palindromes. 

Example:
Input: "A man, a plan, a canal, Panama!"
Output: True

Input: "hello"
Output: False
'''

def is_vowel(character):
    return character.lower() in ['a', 'e', 'i', 'o', 'u']

def is_valid_character(character):
    return character.isalpha() and is_vowel(character)

def is_vowel_palindrome(input_string):
    input_string = ''.join([char.lower() for char in input_string if is_valid_character(char)])
    
    return input_string == input_string[::-1] and any([is_vowel(char) for char in input_string])

# Test the function with the examples
print(is_vowel_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_vowel_palindrome("hello"))  # Output: False
```