'''
Challenge: 
You are given a list of strings. Write a Python function to find the longest common prefix among strings in the list. If there is no common prefix, return an empty string.
'''

def longest_common_prefix(strs):
    if not strs:
        return ""

    min_str = min(strs, key=len)
    for i, char in enumerate(min_str):
        for string in strs:
            if string[i] != char:
                return min_str[:i]
    
    return min_str

# Test the function with some example input
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"