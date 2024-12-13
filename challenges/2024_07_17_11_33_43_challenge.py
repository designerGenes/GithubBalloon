'''
Challenge: Create a function in Python that takes a list of integers as input and returns the second largest number in the list. Your function should work for both positive and negative numbers, and should handle cases where the list has less than 2 elements.
'''

def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least 2 elements"
    
    # Convert the list to a set to remove duplicates, then convert it back to a list
    unique_numbers = list(set(numbers))
    
    # If the list has less than 2 unique elements, return the maximum value
    if len(unique_numbers) < 2:
        return max(unique_numbers)
    
    first_max = second_max = float('-inf')
    
    # Find the two maximum values in the list
    for num in unique_numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
            
    return second_max

# Test the function
numbers = [3, 8, 4, 5, 9, 5, 1, 2]
print(find_second_largest(numbers))  # Output should be 8

numbers = [3, 3, 3]
print(find_second_largest(numbers))  # Output should be 3

numbers = [2]
print(find_second_largest(numbers))  # Output should be "List must have at least 2 elements"
 