'''
Challenge: Write a Python program that generates a maze using a recursive backtracking algorithm. The program should allow the user to specify the dimensions of the maze (e.g. 10x10) and display the maze visually with walls denoted by "#" and empty spaces denoted by ".". The maze should have a start point at the top-left corner and an end point at the bottom-right corner.
'''

import random

def generate_maze(rows, cols):
    def create_grid(rows, cols):
        return [["#" for _ in range(cols)] for _ in range(rows)]

    def is_valid_move(grid, row, col):
        return row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == "#"

    def get_neighbours(row, col):
        neighbours = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        random.shuffle(neighbours)
        return neighbours

    def generate_path(grid, row, col):
        grid[row][col] = "."
        neighbours = get_neighbours(row, col)
        for n_row, n_col in neighbours:
            if is_valid_move(grid, n_row, n_col):
                generate_path(grid, n_row, n_col)

    maze = create_grid(rows, cols)
    generate_path(maze, 0, 0)
    maze[rows-1][cols-1] = "."

    return maze

def display_maze(maze):
    for row in maze:
        print(" ".join(row))

dimensions = input("Enter the dimensions of the maze (e.g. 10x10): ")
rows, cols = map(int, dimensions.split('x'))

maze = generate_maze(rows, cols)
display_maze(maze)
