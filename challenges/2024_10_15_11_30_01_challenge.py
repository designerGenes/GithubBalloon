'''
Challenge:
Create a Python program that simulates a simple text-based Blackjack game between the player and the dealer. The program should allow the player to hit or stand, display the current cards in hand for both the player and dealer, determine the winner based on the Blackjack rules, and keep track of the player's balance. The player starts with an initial balance of 100 chips and can place bets before each round. The game should continue until the player chooses to quit or runs out of chips. Good luck!
'''

import random

# Function to calculate the total value of cards in hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            num_aces += 1
        else:
            value += int(card)
    
    # Adjust for aces
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
            
    return value

# Function to deal a random card
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Function to display cards and total value
def display_hand(cards):
    hand_str = ' '.join(cards)
    hand_value = calculate_hand_value(cards)
    return f'Cards: {hand_str} | Value: {hand_value}'

# Initialize player balance
player_balance = 100

while player_balance > 0:
    print(f'Player balance: {player_balance}')
    player_bet = int(input('Place your bet (minimum bet is 1 chip): '))
    
    if player_bet < 1:
        print('Minimum bet is 1 chip. Please place a valid bet.')
        continue
    if player_bet > player_balance:
        print('You do not have enough chips. Please place a valid bet.')
        continue
        
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    # Player's turn
    player_stand = False
    while not player_stand:
        print('\nYour hand:')
        print(display_hand(player_hand))
        action = input('Do you want to hit (h) or stand (s)? ')
        
        if action.lower() == 'h':
            player_hand.append(deal_card())
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print('Bust! You lose.')
                player_balance -= player_bet
                break
        elif action.lower() == 's':
            player_stand = True
    
    player_value = calculate_hand_value(player_hand)
    
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    
    print('\nDealer\'s hand:')
    print(display_hand(dealer_hand))
    
    dealer_value = calculate_hand_value(dealer_hand)
    
    # Determine the winner
    if player_value > 21:
        pass
    elif dealer_value > 21 or player_value == 21 or player_value > dealer_value:
        print('You win!')
        player_balance += player_bet
    elif player_value < dealer_value:
        print('Dealer wins!')
        player_balance -= player_bet
    else:
        print('Push! It\'s a tie.')
    
    print(f'Player balance: {player_balance}')
    play_again = input('Do you want to play another round? (y/n) ')
    
    if play_again.lower() != 'y':
        break
    
if player_balance <= 0:
    print('You are out of chips. Game over!')
else:
    print('Thank you for playing! See you next time!')
