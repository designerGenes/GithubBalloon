'''
Challenge:
Write a Python function that takes in a list of strings and returns the most common character in the strings. 
If there are multiple characters that are equally common, return all of them in a list. 
The function should ignore whitespace and be case-insensitive.

My solution:
'''

def most_common_chars(strings):
    char_count = {}
    
    for string in strings:
        for char in string.lower().replace(" ", ""):
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    
    max_count = max(char_count.values())
    most_common_chars = [char for char, count in char_count.items() if count == max_count]
    
    return most_common_chars

# Test the function
strings = ["Hello", "World", "Python Programming"]
result = most_common_chars(strings)
print(result)