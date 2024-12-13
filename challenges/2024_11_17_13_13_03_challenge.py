'''
Challenge: Magic Square Verifier

Write a Python function that takes a square matrix (list of lists) as input and returns True if the matrix forms a magic square, and False otherwise. 

A magic square is a square matrix where the sum of the numbers in each row, each column, and both main diagonals are all equal. The numbers in the matrix will be unique integers.

Your function should verify if the matrix is a magic square and return True if it is, and False if it is not.
'''

def is_magic_square(matrix):
    n = len(matrix)
    target_sum = n * (n**2 + 1) // 2
    
    # Calculate sum of the first row to use as reference
    row_sum = sum(matrix[0])
    
    # Check row sums
    for row in matrix:
        if sum(row) != row_sum:
            return False
    
    # Check column sums
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != row_sum:
            return False
    
    # Check main diagonal sum
    if sum(matrix[i][i] for i in range(n)) != row_sum:
        return False
    
    # Check secondary diagonal sum
    if sum(matrix[i][n-1-i] for i in range(n)) != row_sum:
        return False
    
    return True

# Test the function with an example
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(is_magic_square(matrix))  # Output should be True