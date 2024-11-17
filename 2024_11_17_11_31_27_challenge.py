'''
Challenge: You are given a list of strings representing different programming languages. Create a function that sorts these languages based on the number of vowels each language contains, from the highest number of vowels to the lowest. In case of a tie, maintain the original order of the languages in the list.

Example:
Input: ["Python", "Java", "Ruby", "C++", "JavaScript"]
Output: ["Java", "Python", "Ruby", "C++", "JavaScript"]

Input: ["Haskell", "Perl", "Swift", "Rust", "C#"]
Output: ["Haskell", "Swift", "Perl", "Rust", "C#"]
'''

def sort_languages_by_vowels(languages):
    def count_vowels(language):
        vowels = "aeiouAEIOU"
        return sum(1 for letter in language if letter in vowels)
    
    return sorted(languages, key=lambda x: (-count_vowels(x), languages.index(x)))

# Test the function with the given examples
print(sort_languages_by_vowels(["Python", "Java", "Ruby", "C++", "JavaScript"])) 
print(sort_languages_by_vowels(["Haskell", "Perl", "Swift", "Rust", "C#"])) 
