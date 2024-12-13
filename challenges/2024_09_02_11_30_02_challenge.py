'''
Challenge: Magic Square Validator

Create a function that takes a square matrix (list of lists) as input and returns True if it is a magic square, False otherwise. A magic square is a square matrix where the sum of each row, column, and diagonal are all equal. The matrix will always have an odd number of rows and columns. It can be assumed that all elements of the matrix are integers.
'''

def is_magic_square(matrix):
    n = len(matrix)
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check columns
    for i in range(n):
        if sum(matrix[j][i] for j in range(n)) != target_sum:
            return False
    
    # Check main diagonal
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    
    # Check reverse diagonal
    if sum(matrix[i][n-1-i] for i in range(n)) != target_sum:
        return False
    
    return True

# Test the function
matrix1 = [[2, 7, 6], 
           [9, 5, 1], 
           [4, 3, 8]]
print(is_magic_square(matrix1))  # False

matrix2 = [[8, 1, 6], 
           [3, 5, 7], 
           [4, 9, 2]]
print(is_magic_square(matrix2))  # True
