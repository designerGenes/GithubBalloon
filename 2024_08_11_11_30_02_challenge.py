'''
Challenge:
Create a function in Python that takes in a string as input and returns the longest substring that contains only unique characters. For example, if the input is "abcabcbb", the function should return "abc".
'''

def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_substring = ""
    seen = {}

    for end, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substring = s[start:end+1]
        seen[char] = end

    return max_substring

# Test the function with the given example
input_str = "abcabcbb"
output = longest_unique_substring(input_str)
print(output)