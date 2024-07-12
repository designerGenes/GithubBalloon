'''
Challenge: Create a Python program that takes a string as input and returns the most frequent character along with its frequency count. In case of a tie, return all characters with the same highest frequency count. Ignore whitespace and treat uppercase and lowercase characters as the same.
'''

def most_frequent_char(input_string):
    input_string = input_string.lower().replace(" ", "")
    char_frequency = {}
    
    for char in input_string:
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    
    max_frequency = max(char_frequency.values())
    most_frequent_chars = [char for char, freq in char_frequency.items() if freq == max_frequency]
    
    return most_frequent_chars, max_frequency

# Test the function with an example
input_str = "Hello, World!"
result = most_frequent_char(input_str)
print("Most frequent character(s):", result[0])
print("Frequency count:", result[1])