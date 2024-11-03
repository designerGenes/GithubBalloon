'''
Challenge:
Alice has a string containing both lowercase and uppercase letters. Write a Python function to find and return the most common lowercase letter in the string.
If there are multiple lowercase letters that appear the same maximum number of times, return the letter that appears first alphabetically.
If there are no lowercase letters in the string, return None.
'''

def most_common_lowercase_letter(input_string):
    lower_letters = [char for char in input_string if char.islower()]
    
    if not lower_letters:
        return None
    
    letter_count = {}
    for letter in lower_letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    max_count = max(letter_count.values())
    most_common_letters = [letter for letter, count in letter_count.items() if count == max_count]
    
    return min(most_common_letters)

# Test the function
input_string = "HelloWorld"
print(most_common_lowercase_letter(input_string))  # Output: l

input_string = "abcABCabcDEFdef"
print(most_common_lowercase_letter(input_string))  # Output: a

input_string = "HELLO"
print(most_common_lowercase_letter(input_string))  # Output: None