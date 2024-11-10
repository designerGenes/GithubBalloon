'''
Challenge: Create a Python program that takes a list of integers as input and removes all duplicates, while preserving the order of the remaining elements. The program should then print out the updated list without duplicates.
'''

# Input list
input_list = [1, 2, 3, 2, 4, 1, 5, 6, 3]

# Removing duplicates while preserving order
output_list = []
for num in input_list:
    if num not in output_list:
        output_list.append(num)

# Printing the updated list without duplicates
print(output_list)
