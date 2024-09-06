'''
Challenge:
Write a Python function that takes a string as input and returns the frequency of each character in the string as a dictionary. 
Ignore spaces and treat uppercase and lowercase characters as the same. 
For example, given the input "Hello, World!", the output should be {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.

My solution:
'''

def count_characters_frequency(input_str):
    input_str = input_str.lower().replace(" ", "")
    char_frequency = {}
    
    for char in input_str:
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    
    return char_frequency

# Test the function
input_string = "Hello, World!"
print(count_characters_frequency(input_string))