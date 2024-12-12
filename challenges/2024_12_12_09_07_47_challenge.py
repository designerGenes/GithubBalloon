'''
Challenge: You are tasked with implementing a program that can detect and count the number of valid anagrams within a given list of strings. Anagrams are words or phrases that are formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

Your program should take in a list of strings as input and output the total count of valid anagrams found within the list. Remember that a single word cannot be considered an anagram of itself.

For example:
Input: ["listen", "silent", "enlist", "hello", "world"]
Output: 2

In this example, "listen", "silent", and "enlist" form a group of valid anagrams, while "hello" and "world" do not have any valid anagrams within the list.
'''

def count_valid_anagrams(words):
    anagram_count = 0
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if sorted(words[i]) == sorted(words[j]) and words[i] != words[j]:
                anagram_count += 1
    
    return anagram_count

# Test the function with the given example
input_words = ["listen", "silent", "enlist", "hello", "world"]
print(count_valid_anagrams(input_words))