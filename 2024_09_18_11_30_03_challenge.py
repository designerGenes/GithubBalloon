'''
Challenge: 
Create a Python function that takes in a string as input and returns the count of how many words in the string contain the letter 'e' exactly 3 times. 
The input string will only contain alphabetic characters and spaces. 
For example, if the input string is "elephant exercise elegant", the function should return 2, as both "elephant" and "exercise" contain the letter 'e' exactly 3 times.
'''

def count_words_with_three_es(input_str):
    count = 0
    words = input_str.split()
    for word in words:
        if word.count('e') == 3:
            count += 1
    return count

# Test the function with the given example
input_str = "elephant exercise elegant"
print(count_words_with_three_es(input_str))
