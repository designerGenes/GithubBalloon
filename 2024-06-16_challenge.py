Challenge:
Write a Python program that simulates a simple text-based adventure game. The game should include at least three different rooms that the player can move between, each with its own description and potential interactions. The player should be able to pick up items, use items, and encounter obstacles or enemies. The goal of the game is for the player to navigate through the rooms and reach a specific final room in order to win. The game should provide feedback to the player based on their actions and progress.

My solution:
```
import random

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []

    def __str__(self):
        return f'{self.name}\n{self.description}'

class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            return f'You used {item}.'
        else:
            return f'You don\'t have {item} in your inventory.'

def game():
    # Define rooms
    room1 = Room('Room 1', 'You are in a dark room with a door to the east.', ['key'])
    room2 = Room('Room 2', 'You entered a dimly lit room with a chest.', ['potion'])
    room3 = Room('Final Room', 'Congratulations! You reached the final room.')

    # Connect rooms
    rooms = {
        'Room 1': {'east': room2},
        'Room 2': {'west': room1, 'east': room3},
        'Final Room': {'west': room2}
    }

    current_room = room1
    player = Player()

    while current_room != room3:
        print(current_room)
        action = input('What would you like to do? (e.g. move, take, use): ')
        if action == 'move':
            direction = input('Which direction would you like to go? ')
            if direction in rooms[current_room.name]:
                current_room = rooms[current_room.name][direction]
            else:
                print('You cannot go that way.')
        elif action == 'take':
            item = input('What item would you like to take? ')
            if item in current_room.items:
                player.add_to_inventory(item)
                current_room.items.remove(item)
                print(f'You picked up {item}.')
            else:
                print('There is no such item in this room.')
        elif action == 'use':
            item = input('Which item would you like to use? ')
            result = player.use_item(item)
            print(result)
        else:
            print('Invalid action. Please try again.')

    print(current_room)

if __name__ == '__main__':
    game()
```
The above code defines a simple text-based adventure game where the player can navigate through different rooms, pick up items, and use items to reach the final room. The rooms are connected through a map and the player's actions determine the progress in the game.