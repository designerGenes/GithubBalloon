'''
Challenge:
Write a Python function that takes a string as input and returns the first non-repeating character in the string. If all characters are repeated, return "_" (underscore).
'''

def first_non_repeating_character(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in input_string:
        if char_count[char] == 1:
            return char
        
    return "_"

# Test the function
input_string = "hello"
print(first_non_repeating_character(input_string))  # Output should be 'h'

input_string = "aabbcc"
print(first_non_repeating_character(input_string))  # Output should be '_'
