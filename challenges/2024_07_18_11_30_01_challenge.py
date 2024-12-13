'''
Challenge: Create a Python function that takes in a list of integers and returns the second largest number in the list. If there is no second largest number, the function should return None.
'''

def second_largest(lst):
    if len(lst) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest
