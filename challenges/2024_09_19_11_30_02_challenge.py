'''
Challenge:
Create a program that simulates a simple text-based adventure game. The game should have multiple rooms that the player can navigate through, each with its own description, items to interact with, and possible actions to take. The player should be able to pick up items, use items, and solve puzzles to progress through the game. The game should have a clear win condition and provide feedback to the player along the way. The player should also have the ability to save and load their progress in the game.

My solution:
'''

# Define the different rooms in the game
rooms = {
    'start': {
        'description': 'You are in a dark room. There is a door to the north.',
        'items': ['torch'],
        'exits': {'north': 'hallway'}
    },
    'hallway': {
        'description': 'You are in a long hallway.',
        'items': ['key'],
        'exits': {'south': 'start', 'north': 'exit'}
    },
    'exit': {
        'description': 'You have found the exit! Congratulations, you win!',
        'items': [],
        'exits': {}
    }
}

# Player inventory
inventory = []

# Current room
current_room = 'start'

# Function to move to a different room
def move(direction):
    global current_room
    if direction in rooms[current_room]['exits']:
        current_room = rooms[current_room]['exits'][direction]
        print(rooms[current_room]['description'])
    else:
        print('You cannot go that way.')

# Function to pick up an item
def pick_up(item):
    if item in rooms[current_room]['items']:
        rooms[current_room]['items'].remove(item)
        inventory.append(item)
        print(f'You picked up the {item}.')
    else:
        print('There is no such item here.')

# Function to use an item
def use_item(item):
    if item in inventory:
        if current_room == 'exit' and item == 'key':
            print('You unlocked the exit! Congratulations, you win!')
        else:
            print(f'You used the {item}.')
            # Add more item interactions or puzzles here
    else:
        print('You do not have that item.')

# Game loop
print(rooms[current_room]['description'])
while True:
    action = input('\nWhat would you like to do? (move/pick up/use/quit): ')
    
    if action == 'quit':
        print('Thanks for playing!')
        break
    
    if action == 'move':
        direction = input('Which direction would you like to go? ')
        move(direction)
    
    if action == 'pick up':
        item = input('Which item would you like to pick up? ')
        pick_up(item)
    
    if action == 'use':
        item = input('Which item would you like to use? ')
        use_item(item)
