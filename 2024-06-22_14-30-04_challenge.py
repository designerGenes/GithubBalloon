"""
Challenge:
Write a Python program that generates a list of 10 random numbers between 1 and 100, sorts the list in descending order, removes any duplicates, and then calculates and prints the sum of the squared values of the remaining unique numbers.

My solution:
"""

import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Sort the list in descending order
random_numbers.sort(reverse=True)

# Remove duplicates by converting the list to a set
unique_numbers = set(random_numbers)

# Calculate the sum of squared unique numbers
sum_squared_values = sum(num**2 for num in unique_numbers)

print(sum_squared_values)