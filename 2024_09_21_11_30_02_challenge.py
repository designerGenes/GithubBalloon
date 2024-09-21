'''
Challenge: Implement a function in Python that takes in a list of words and returns the shortest word(s) in the list. If there are multiple words with the same shortest length, return all of them in a list. The function should ignore any punctuation and consider uppercase and lowercase letters as equal (e.g., "A" and "a" are considered the same letter).

My solution:
'''

def shortest_words(words):
    words = [word.lower().strip('.,!?') for word in words]
    min_length = min(len(word) for word in words)
    shortest_words = [word for word in words if len(word) == min_length]
    return shortest_words

# Test the function with an example
words_list = ["apple", "banana", "kiwi", "plum", "fig"]
print(shortest_words(words_list))  # Output should be ['kiwi']