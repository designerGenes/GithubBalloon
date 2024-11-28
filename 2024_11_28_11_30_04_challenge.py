'''
Challenge: 
Create a Python program that simulates a game of Hangman. The program should randomly select a word from a predefined list, display the secret word with underscores representing the missing letters, allow the user to guess letters one at a time, track the incorrect guesses, and reveal the correct letters in the word as they are guessed. The player should have a limited number of incorrect guesses before losing the game.

My solution:
'''

import random

def select_word():
    word_list = ['python', 'hangman', 'developer', 'challenge', 'program', 'coding']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    secret_word = select_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_word(secret_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Incorrect guess! {max_incorrect_guesses - incorrect_guesses} guesses remaining.")
        
        print(display_word(secret_word, guessed_letters))

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word.")
            break

        if incorrect_guesses == max_incorrect_guesses:
            print("Out of guesses. The word was: ", secret_word)
            break

hangman()
