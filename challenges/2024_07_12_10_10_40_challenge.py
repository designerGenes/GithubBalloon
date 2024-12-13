'''
Challenge: 
You are given a list of strings. Write a Python function to return the most common prefix among all strings in the list. If there is no common prefix, return an empty string.

Implement this function in 100 lines of code or less.
'''

def find_common_prefix(strs):
    if not strs:
        return ""

    min_length = min(len(s) for s in strs)
    prefix = ""

    for i in range(min_length):
        if all(s[i] == strs[0][i] for s in strs):
            prefix += strs[0][i]
        else:
            break

    return prefix

# Test the function with an example
strings = ["flower", "flow", "flight"]
print(find_common_prefix(strings))  # Output: "fl"