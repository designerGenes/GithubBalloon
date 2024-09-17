'''
Challenge: 
You are given a list of integers representing the heights of buildings in a city skyline. Write a Python function to calculate the total area of the skyline when viewed from the side. Assume each building has a width of 1 unit. The skyline is formed by overlapping the buildings in the list.
'''

def calculate_skyline_area(heights):
    if not heights:
        return 0
    
    total_area = 0
    max_height = max(heights)
    max_height_index = heights.index(max_height)

    left_height = 0
    for i in range(max_height_index):
        if heights[i] > left_height:
            left_height = heights[i]
        total_area += left_height

    right_height = 0
    for i in range(len(heights) - 1, max_height_index, -1):
        if heights[i] > right_height:
            right_height = heights[i]
        total_area += right_height

    total_area += max_height

    return total_area

# Test the function with an example
heights = [3, 7, 2, 3, 5]
print(calculate_skyline_area(heights))
