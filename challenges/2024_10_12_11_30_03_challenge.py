'''
Challenge: 
Create a Python program that takes a string as input and prints out all possible permutations of the characters in the string.

My solution:
'''

from itertools import permutations

def get_permutations(input_str):
    perms = permutations(input_str)
    for perm in perms:
        print(''.join(perm))

# Test the function with an example
input_str = "abc"
get_permutations(input_str)