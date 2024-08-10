'''
Challenge: Create a Python function that takes in a string as input and returns the most common character in the string. If there are multiple characters with the same highest frequency, return the one that appears first in the string. Ignore whitespace and consider uppercase and lowercase letters as the same character.
'''

def most_common_character(input_string):
    input_string = input_string.lower()  # Convert the input string to lowercase
    input_string = input_string.replace(" ", "")  # Remove whitespace

    char_count = {}  # Dictionary to store character counts

    for char in input_string:
        if char.isalpha():  # Check if character is a letter
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    max_count = max(char_count.values())  # Find the highest frequency

    most_common_chars = [char for char, count in char_count.items() if count == max_count]  # Find characters with highest frequency

    for char in input_string:
        if char in most_common_chars:
            return char
'''

(SOLUTION)