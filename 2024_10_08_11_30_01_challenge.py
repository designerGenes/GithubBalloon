'''
Challenge:
Create a program that simulates a game of Rock, Paper, Scissors between a player and a computer. 
The computer's choice should be randomly generated. 
The program should ask the player for their choice and then determine the winner based on the traditional rules 
(Rock beats Scissors, Scissors beats Paper, Paper beats Rock). 
The program should keep track of the score and continue playing multiple rounds until the player decides to quit. 
At the end, the program should display the final score.
'''

import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def update_score(result, score):
    if result == "Player wins!":
        score[0] += 1
    elif result == "Computer wins!":
        score[1] += 1

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    score = [0, 0]
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to end the game: ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        update_score(result, score)

    print(f"Final Score - Player: {score[0]}, Computer: {score[1]}")

rock_paper_scissors()
