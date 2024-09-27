'''
Challenge:
Write a Python function that takes in a string as input and returns the longest substring that contains at most two distinct characters. 
For example, given the input "abaccc", the function should return "ccc" as it is the longest substring with at most two distinct characters. 
Your function should be able to handle both uppercase and lowercase letters.
'''

def longest_substring_with_two_distinct_chars(s):
    if not s:
        return ""

    start = 0
    max_length = 0
    max_start = 0
    char_dict = {}

    for end, char in enumerate(s):
        char_dict[char] = end

        if len(char_dict) > 2:
            current_length = end - start
            if current_length > max_length:
                max_length = current_length
                max_start = start

            del_key = min(char_dict, key=char_dict.get)
            start = char_dict[del_key] + 1
            del char_dict[del_key]

    if len(s) - start > max_length:
        max_start = start

    return s[max_start: max_start + max_length]


# Test the function with example input
input_str = "abaccc"
print(longest_substring_with_two_distinct_chars(input_str))