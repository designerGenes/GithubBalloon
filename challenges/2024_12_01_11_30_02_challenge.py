'''
Challenge:
Create a program that simulates a game of Tic-Tac-Toe between two players. The program should display the game board,
ask players to input their moves, and check for a win or a tie after each move. The game should continue until one player wins
or it's a tie. Lastly, the program should print out the winner or indicate a tie at the end of the game.
'''

# Tic-Tac-Toe game implementation
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'

    def print_board(self):
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |")
            print("-------------")

    def check_winner(self):
        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],
                            [0, 4, 8], [2, 4, 6]]
        for comb in win_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] == self.current_player:
                return True
        return False

    def check_tie(self):
        return all(cell != ' ' for cell in self.board)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1

            if self.board[move] == ' ':
                self.board[move] = self.current_player
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.check_tie():
                    self.print_board()
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("That cell is already taken, please try again.")

# Play the game
game = TicTacToe()
game.play_game()
