'''
Challenge: Write a Python program that takes a string as input and outputs the longest substring of consecutive vowels (a, e, i, o, u) in the input string. If there are multiple substrings with the same length, return the first one found.
'''

def longest_vowel_substring(s):
    vowels = "aeiou"
    max_length = 0
    curr_length = 0
    start_index = 0
    max_start_index = 0

    for i in range(len(s)):
        if s[i] in vowels:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
                max_start_index = start_index
        else:
            curr_length = 0
            start_index = i + 1

    return s[max_start_index:max_start_index + max_length] if max_length > 0 else ""

# Test the function
input_string = "leetcodeisawesome"
output = longest_vowel_substring(input_string)
print(output)
