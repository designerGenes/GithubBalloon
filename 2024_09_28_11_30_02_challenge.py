'''
Challenge: Create a program that simulates a simple text-based adventure game. The game should have multiple rooms that the player can move between, items that can be picked up and used, and puzzles to solve in order to progress. Ensure the player can interact with the environment by examining objects and making choices that affect the outcome of the game. The game should have a clear objective and a way for the player to win or lose. Aim to make the game engaging and fun to play within the 100-line limit.
'''

import time

# Define the classes
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.items = []

    def connect(self, direction, room):
        self.connected_rooms[direction] = room

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, description, use_text):
        self.name = name
        self.description = description
        self.use_text = use_text

    def use(self):
        return self.use_text

# Define the game logic
def game_start():
    # Define rooms
    room1 = Room("Living Room", "A cozy living room.")
    room2 = Room("Kitchen", "A spacious kitchen.")
    
    # Connect rooms
    room1.connect("east", room2)
    room2.connect("west", room1)
    
    # Create items
    key = Item("Key", "A shiny golden key.", "You unlocked a secret door!")
    note = Item("Note", "A crumpled piece of paper with a clue.", "You solved the puzzle!")
    
    # Add items to rooms
    room1.add_item(key)
    room2.add_item(note)
    
    # Initialize game variables
    current_room = room1
    inventory = []
    
    # Game loop
    while True:
        print("You are in the", current_room.name)
        print(current_room.description)
        
        if current_room.items:
            for item in current_room.items:
                print("You see a", item.name)
        
        # Player input
        move = input("Where do you want to go? (east/west) Type 'quit' to exit: ")
        
        if move == "quit":
            break
        elif move in current_room.connected_rooms:
            current_room = current_room.connected_rooms[move]
        else:
            print("Invalid move!")
        
        # Item interaction
        action = input("Do you want to pick up an item? (y/n): ")
        
        if action == 'y':
            item_name = input("Enter the name of the item you want to pick up: ")
            for item in current_room.items:
                if item_name.lower() == item.name.lower():
                    inventory.append(item)
                    current_room.items.remove(item)
                    print("You picked up the", item.name)
                    print(item.use())
                    break
            else:
                print("Item not found in the room!")
        
        time.sleep(1)

game_start()
