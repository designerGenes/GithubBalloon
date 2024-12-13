'''
Challenge:
Create a Python program that simulates a game of Tic Tac Toe between two players. The program should display the Tic Tac Toe board, allow players to take turns entering their moves, check for a winner or a draw after each move, and display the outcome at the end of the game. The program should handle invalid moves and display appropriate error messages.
'''

# Tic Tac Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ':
        return board[0][0]
    
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter col (0, 1, 2): "))

        if is_valid_move(board, row, col):
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    play_game()
