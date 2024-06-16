Challenge:
Create a program that generates a random list of 10,000 integers between 1 and 100, then sorts the list using the bubble sort algorithm. Finally, count and print the number of swaps performed during the sorting process. Your program should be implemented in 100 lines of Python code or less.

My solution:
```python
import random

def generate_random_list(length, low, high):
    return [random.randint(low, high) for _ in range(length)]

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, swaps

if __name__ == "__main__":
    random_list = generate_random_list(10000, 1, 100)
    sorted_list, num_swaps = bubble_sort(random_list.copy())

    print(f"Random List: {random_list[:10]}...")  # Displaying first 10 elements
    print(f"Sorted List: {sorted_list[:10]}...")
    print(f"Number of Swaps: {num_swaps}")
```
