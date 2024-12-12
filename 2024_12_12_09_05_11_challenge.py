'''
Challenge:
Write a Python function that takes in a string and returns the first non-repeating character. If all characters are repeating, return None. 
Your function should be named `find_first_non_repeating_char` and should handle both uppercase and lowercase letters.

My solution:
'''

def find_first_non_repeating_char(s):
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char.lower()] == 1:
            return char
    
    return None

# Test the function
print(find_first_non_repeating_char("hello"))  # Output should be 'h'
print(find_first_non_repeating_char("leetcode"))  # Output should be 'l'
print(find_first_non_repeating_char("aabbcc"))  # Output should be None