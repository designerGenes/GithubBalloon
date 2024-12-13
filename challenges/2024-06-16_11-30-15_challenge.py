Challenge:
Write a Python program that takes a list of integers as input and returns the mode of the list (the number that appears most frequently). Your program should handle cases where multiple numbers have the same highest frequency, in which case it should return the smallest number among them.

My solution:
```python
def find_mode(input_list):
    num_count = {}
    
    # Count the frequency of each number in the input list
    for num in input_list:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Find the number(s) with the highest frequency
    max_freq = max(num_count.values())
    modes = [num for num, freq in num_count.items() if freq == max_freq]
    
    # Return the smallest number among the modes
    return min(modes)

# Test the function with an example list
input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Mode of the list:", find_mode(input_list))
```
You can test the function with different input lists to check if it returns the correct mode according to the specified conditions.