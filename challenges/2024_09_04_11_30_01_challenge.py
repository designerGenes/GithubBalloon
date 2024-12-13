'''
Challenge:
Create a Python program that takes a list of words as input and returns the longest word that can be formed by concatenating other words from the list. Each word in the list can be used only once in the concatenation process. If multiple longest words can be formed, return the one that appears first in the input list.
'''

def is_concatenated_word(word, word_set):
    if word in word_set:
        return True
    for i in range(1, len(word)):
        prefix = word[0:i]
        suffix = word[i:]
        if prefix in word_set and is_concatenated_word(suffix, word_set):
            return True
    return False

def longest_concatenated_word(words):
    word_set = set(words)
    words.sort(key=lambda x: (-len(x), words.index(x)))
    for word in words:
        word_set.remove(word)
        if is_concatenated_word(word, word_set):
            return word

# Example
words_list = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(longest_concatenated_word(words_list))