'''
Challenge:
Create a function in Python that takes in a string as input and returns the frequency of each character in the string as a dictionary. Ignore spaces and punctuation, and make the function case-insensitive.

My solution:
'''

def char_frequency(input_str):
    freq_dict = {}
    for char in input_str.lower():
        if char.isalnum():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict

# Test the function
input_string = "Hello, World!"
output = char_frequency(input_string)
print(output)