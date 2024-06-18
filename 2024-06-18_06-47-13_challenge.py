"""
Challenge:
Write a Python program that takes a list of words as input and returns the longest word(s) in the list.
If there are multiple words with the same maximum length, return all of them in a list.
The program should ignore punctuation and consider uppercase and lowercase letters as the same.
Your program should be able to handle ties, special characters, and empty strings in the input list.

My solution:
"""

def find_longest_words(words):
    clean_words = [''.join(filter(str.isalnum, word.lower())) for word in words]  # Removing punctuation and converting to lowercase
    max_length = max(len(word) for word in clean_words)  # Finding the maximum length of words
    
    longest_words = [word for word in clean_words if len(word) == max_length]  # Finding all longest words with maximum length
    return longest_words

# Test the function
words_list = ["Python", "is", "a", "Powerful", "Programming", "Language"]
print(find_longest_words(words_list))

words_list2 = ["Python!!", "is,", "a...", "Powerful.", "programming", "language!"]
print(find_longest_words(words_list2))

words_list3 = ["Python", "", "is", "an", "AWESOME", "Language"]
print(find_longest_words(words_list3))