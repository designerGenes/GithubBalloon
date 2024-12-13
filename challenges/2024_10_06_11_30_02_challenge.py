'''
Challenge: 
Create a Python function that takes in a string as input and returns the first non-repeating character in the string. If all characters are repeated, return None. The function should handle both uppercase and lowercase letters as the same character (case-insensitive).
'''

def first_non_repeating_char(s):
    s = s.lower()
    char_count = {}
    
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Test the function
input_string = "aABbccccdeEFF"
print(first_non_repeating_char(input_string))  # Output should be 'd'