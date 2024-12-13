'''
Challenge: Create a Python function that takes in a string as input and returns the most common character in the string. 
If there are multiple characters that are equally common and have the highest frequency, return the character that appears first in the string. 
Ignore whitespace and consider uppercase and lowercase letters as the same character.
'''

def most_common_char(input_string):
    input_string = input_string.lower().replace(" ", "")
    char_freq = {}
    
    for char in input_string:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    max_freq = max(char_freq.values())
    most_common_chars = [char for char, freq in char_freq.items() if freq == max_freq]
    
    for char in input_string:
        if char in most_common_chars:
            return char
            break

# Test the function
input_str = "Hello, World!"
result = most_common_char(input_str)
print(result)
