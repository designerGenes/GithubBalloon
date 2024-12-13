'''
Challenge: Write a Python function that takes in a string as input and returns the longest substring without repeating characters. 
For example, if the input string is "abcabcbb", the function should return "abc".
'''

def longest_substring_without_repeating_chars(s):
    if not s:
        return ""

    start = max_length = 0
    char_index_map = {}

    for i in range(len(s)):
        if s[i] in char_index_map and start <= char_index_map[s[i]]:
            start = char_index_map[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        char_index_map[s[i]] = i

    return s[start:start + max_length]

# Test the function with example input
print(longest_substring_without_repeating_chars("abcabcbb"))  # Output: "abc"
