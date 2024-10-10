'''
Challenge:
Create a Python function that takes a string as input and returns the longest substring without repeating characters.

My solution:
'''

def longest_substring_without_repeating_chars(s):
    start = 0
    max_length = 0
    char_index = {}
    
    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length