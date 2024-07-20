'''
Challenge:
Given a list of integers, write a Python function to find the second largest element in the list. 
The function should return the second largest element. 
If there is no second largest element, return None. 
Your function should work efficiently and handle edge cases such as empty lists or lists with repeated elements.
'''

def find_second_largest(nums):
    if not nums or len(nums) < 2:
        return None
    
    # Remove duplicates and sort in descending order
    unique_nums = sorted(set(nums), reverse=True)
    
    # Check if there is a second largest element
    return unique_nums[1] if len(unique_nums) > 1 else None

# Test the function
print(find_second_largest([1, 2, 3, 4, 5]))  # Output: 4
print(find_second_largest([5, 5, 5, 5, 5]))  # Output: None
print(find_second_largest([3, 1, 4, 3, 2]))  # Output: 3
print(find_second_largest([]))  # Output: None