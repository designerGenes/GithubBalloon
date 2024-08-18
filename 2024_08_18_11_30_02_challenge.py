'''
Challenge: Create a Python program that takes in a list of words and returns the shortest word. If there are multiple shortest words, return all of them in a list. Remember to handle cases where the input list is empty. The program should be implemented in 100 lines of code or less.
'''

def find_shortest_words(words):
    if not words:
        return []
    
    shortest_len = min(len(word) for word in words)
    shortest_words = [word for word in words if len(word) == shortest_len]
    
    return shortest_words

# Test the function with some sample data
words_list = ["apple", "banana", "pear", "kiwi", "grape"]
print(find_shortest_words(words_list))  # Output: ['pear', 'kiwi']

empty_list = []
print(find_shortest_words(empty_list))  # Output: []