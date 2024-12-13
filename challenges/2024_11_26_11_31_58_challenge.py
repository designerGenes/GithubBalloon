'''
Challenge: Create a program that takes a string as input and returns the frequency of each character in the string as a dictionary. The program should ignore spaces and be case-insensitive. For example, if the input is "Hello, World!", the output should be {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1, 'd': 1}.
'''

# My solution:
def count_characters_frequency(input_string):
    frequency_dict = {}
    input_string = input_string.lower().replace(" ", "")
    
    for char in input_string:
        if char.isalpha():
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    return frequency_dict

# Test the function with the example input
input_string = "Hello, World!"
result = count_characters_frequency(input_string)
print(result)