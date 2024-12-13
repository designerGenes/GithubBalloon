Challenge:
'''
Create a program that takes a list of words as input and returns the longest word(s) that can be formed by concatenating other words from the list. Each word can be used multiple times if needed. If there are multiple longest words, return all of them. For example, given the input ["cat", "cats", "catsdogcats", "dog", "dogcatsdog"], the output should be ["catsdogcats", "dogcatsdog"].
'''

My solution:
SOLUTION
```python
def longest_concatenated_words(words):
    word_set = set(words)
    words.sort(key=lambda x: len(x), reverse=True)

    def is_concatenated(word):
        if word in word_set and word != words[0]:
            return True
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and is_concatenated(suffix):
                return True
        return False

    result = []
    for word in words:
        if is_concatenated(word):
            result.append(word)
    
    return result

# Test the function with the given example
input_words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog"]
output = longest_concatenated_words(input_words)
print(output)
```