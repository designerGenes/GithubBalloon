Challenge:
Write a Python program that takes a string input from the user and checks if it is a palindrome. Ignore any non-alphanumeric characters and case sensitivity when checking for palindromes. For example, "A man, a plan, a canal, Panama!" should be considered a palindrome. Your program should output "Yes" if the input string is a palindrome and "No" if it is not.

My solution:
```
def is_palindrome(s):
    # Create a clean string with only alphanumeric characters
    clean_s = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the clean string is a palindrome
    return clean_s == clean_s[::-1]

# Get user input
user_input = input("Enter a string: ")

# Check if the input string is a palindrome and ignore non-alphanumeric characters and case sensitivity
if is_palindrome(user_input):
    print("Yes")
else:
    print("No")
```
