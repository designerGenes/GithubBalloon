'''
Challenge: Create a program that simulates a simplified game of Battleship where a player 
can place their ships on a 5x5 grid and then try to sink the computer's hidden ships by 
guessing coordinates. The game should include a visual representation of the grid, allow 
the player to input their ship coordinates, and provide feedback on hit or miss for each guess. 
The player wins if they sink all the computer's ships before running out of guesses.
'''

import random

# Initialize the game grid
player_grid = [['-' for _ in range(5)] for _ in range(5)]
computer_grid = [['-' for _ in range(5)] for _ in range(5)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Function to check the validity of coordinates
def is_valid(row, col):
    return 0 <= row < 5 and 0 <= col < 5

# Function to place player's ships
def place_ships(grid):
    for _ in range(2):
        row = int(input("Enter row for ship " + str(_ + 1) + ": "))
        col = int(input("Enter column for ship " + str(_ + 1) + ": "))
        if is_valid(row, col):
            grid[row][col] = 'S'
        else:
            print("Invalid coordinates. Try again.")
            place_ships(grid)

# Function to generate computer's ships
def generate_ships(grid):
    for _ in range(2):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        grid[row][col] = 'S'

# Function to play the game
def play_game():
    player_attempts = 6
    generate_ships(computer_grid)

    print("Welcome to Battleship!\n")
    print("Let's place your ships on the grid:")
    print_grid(player_grid)
    place_ships(player_grid)

    print("\nLet the game begin!\n")
    while player_attempts > 0:
        print("Player Grid:")
        print_grid(player_grid)
        print("Computer Grid:")
        print_grid(computer_grid)

        guess_row = int(input("Enter row to guess: "))
        guess_col = int(input("Enter column to guess: "))

        if is_valid(guess_row, guess_col):
            if computer_grid[guess_row][guess_col] == 'S':
                print("HIT! You sank a ship!")
                computer_grid[guess_row][guess_col] = 'X'
            else:
                print("MISS! Try again.")
            player_attempts -= 1
        else:
            print("Invalid coordinates. Try again.")

        if all(['S' not in row for row in computer_grid]):
            print("Congratulations! You sank all the ships. You win!")
            break

    if player_attempts == 0:
        print("Out of attempts. Game Over.")

# Start the game
play_game()
