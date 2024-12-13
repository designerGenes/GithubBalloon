'''
Challenge: 
Create a program that reads a text file and outputs the top 5 most common words along with their frequencies in descending order. 
Ignore case sensitivity and consider any non-alphabetic characters as word boundaries.
'''

filename = 'sample_text.txt'

def clean_word(word):
    return ''.join(char for char in word if char.isalpha()).lower()

word_freq = {}

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            cleaned_word = clean_word(word)
            if cleaned_word:
                word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1

top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

for word, freq in top_words:
    print(f'{word}: {freq}')