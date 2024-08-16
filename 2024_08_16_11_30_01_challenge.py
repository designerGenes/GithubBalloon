'''
Challenge: Write a Python program that takes a string as input and returns the frequency of each character in the string, sorted in descending order.
'''

def character_frequency(input_string):
    char_freq = {}
    
    # Count frequency of each character
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
            
    # Sort the characters by frequency in descending order
    sorted_char_freq = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}
    
    return sorted_char_freq

# Test the function
input_str = "hello, world!"
result = character_frequency(input_str)
print(result)
