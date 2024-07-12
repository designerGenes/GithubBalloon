'''
Challenge: Write a Python function that takes in a list of integers and returns the majority element if it exists. The majority element is the element that appears more than ⌊n/2⌋ times in the list, where n is the length of the list. If there is no majority element, return None.
'''

def find_majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = nums.count(candidate)
    if count > len(nums) // 2:
        return candidate
    else:
        return None

# Test the function
print(find_majority_element([1, 2, 2, 3, 2, 2, 4]))  # Output: 2
print(find_majority_element([1, 2, 3, 4, 5]))  # Output: None
print(find_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]))  # Output: 4