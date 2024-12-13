'''
Challenge: Implement a program that reads in a text file containing a list of words and outputs the frequency of each word in descending order. Make sure to remove any punctuation marks and ignore letter casing (e.g. "Apple" and "apple" should be considered the same word).
'''

# My solution:
import re
from collections import Counter

def word_frequency(file_name):
    words = []
  
    # Read the file content and convert all words to lowercase
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            words.extend(re.findall(r'\b\w+\b', line))

    # Count the frequency of each word
    word_freq = Counter(words)
    
    # Sort the words by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_word_freq

file_name = 'words.txt'  # Change this to the name of your text file
result = word_frequency(file_name)

for word, count in result.items():
    print(f'{word}: {count}')
