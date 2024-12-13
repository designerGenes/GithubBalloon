'''
Challenge:
Create a function in Python that takes in a string as input and returns the frequency of each character in the string as a dictionary. The function should ignore spaces and be case-insensitive. For example, for input "Hello, World!", the function should return {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1, 'd': 1, 'w': 1}.
'''

def char_frequency(string):
    string = string.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    freq_dict = {}  # Dictionary to store character frequencies

    for char in string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1

    return freq_dict

# Test the function with the given example
input_string = "Hello, World!"
print(char_frequency(input_string))