"""
Challenge:
Create a Python program that reads a text file containing a list of words and determines the longest word that is a palindrome. 
The program should ignore case sensitivity and only consider alphanumeric characters in the words. If multiple palindromes of the 
same length are found, the program should return the first one encountered in the file. The program should output the longest 
palindrome found along with its length.

My solution:
"""

import re

def is_palindrome(word):
    word = re.sub('[^a-zA-Z0-9]', '', word).lower()
    return word == word[::-1]

def longest_palindrome(words_file):
    longest_palindrome = ""
    max_length = 0

    with open(words_file, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                if is_palindrome(word) and len(word) > max_length:
                    longest_palindrome = word
                    max_length = len(word)

    return longest_palindrome, max_length

words_file = "words.txt"
longest_palindrome, length = longest_palindrome(words_file)
print(f"Longest Palindrome: {longest_palindrome}, Length: {length}")