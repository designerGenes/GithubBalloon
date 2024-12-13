'''
Challenge:
Implement a function in Python that takes in a string as input and returns the longest palindrome substring found within the input string. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). If there are multiple longest palindrome substrings, return the first one found. If no palindrome substring is found, return an empty string.
'''

def longest_palindrome_substring(input_string):
    def expand_around_center(left, right):
        while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
            left -= 1
            right += 1
        return input_string[left+1:right]  # Return the palindrome substring
    
    longest_palindrome = ""
    
    for i in range(len(input_string)):
        palindrome1 = expand_around_center(i, i)  # For odd length palindromes
        palindrome2 = expand_around_center(i, i+1)  # For even length palindromes
        
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2
    
    return longest_palindrome

# Test the function
input_string = "babad"
print(longest_palindrome_substring(input_string))  # Output: "aba" or "bab"

input_string = "cbbd"
print(longest_palindrome_substring(input_string))  # Output: "bb"

input_string = "abc"
print(longest_palindrome_substring(input_string))  # Output: "" (No palindrome substring found)
'''