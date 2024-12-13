'''
Challenge: Create a Python function that takes a string as input and returns the most common letter in the string as well as its frequency count. If there are multiple letters with the same highest frequency count, return all of them in alphabetical order. Ignore any characters that are not letters.
'''

def most_common_letter(input_string):
    letter_count = {}
    max_count = 0
    
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            max_count = max(max_count, letter_count[char])
    
    most_common_letters = [letter for letter, count in letter_count.items() if count == max_count]
    
    return sorted(most_common_letters), max_count

# Test the function
input_string = "Hello, World!"
result = most_common_letter(input_string)
print(result)