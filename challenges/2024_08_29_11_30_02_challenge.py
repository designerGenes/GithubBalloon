'''
Challenge:
Write a Python program that takes a list of words as input and returns the longest word in the list. If there are multiple words with the same maximum length, return the first one encountered.

My solution:
'''

def find_longest_word(word_list):
    max_length = 0
    longest_word = ""
    
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
            
    return longest_word

# Test the function
word_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(find_longest_word(word_list))