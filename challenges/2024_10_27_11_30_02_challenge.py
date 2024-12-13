'''
Challenge: Create a Python program that simulates a simple text-based game where the player navigates through different rooms of a house. Each room has specific items to interact with and actions to take, such as picking up objects or using tools. The player can move between rooms by typing commands like "go to [room name]" and can win the game by reaching a final room with a specific item. The game should have a clear set of rules, provide descriptive feedback to the player's actions, and include at least 5 rooms with unique characteristics. Make the game engaging and interactive within the 100-line limit.
'''

import time

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        if len(self.items) > 0:
            print("You see the following items in the room:")
            for item in self.items:
                print("- " + item)
        else:
            print("There are no items in this room.")

    def __str__(self):
        return self.description


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def pick_up_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print("You picked up the", item)
        else:
            print("The item is not in this room.")

    def show_inventory(self):
        if len(self.inventory) > 0:
            print("You are carrying the following items:")
            for item in self.inventory:
                print("- " + item)
        else:
            print("Your inventory is empty.")


# Creating rooms
living_room = Room("Living Room", "A cozy room with a fireplace.", items=["Key"])
kitchen = Room("Kitchen", "A well-equipped kitchen with a dining table.", items=["Knife"])
bedroom = Room("Bedroom", "A spacious bedroom with a king-sized bed.", items=["Flashlight"])
bathroom = Room("Bathroom", "A modern bathroom with a bathtub and shower.", items=["Towel"])
backyard = Room("Backyard", "A lush green backyard with a swing.", items=["Map"])

# Setting room connections
living_room.connections = {"kitchen": kitchen}
kitchen.connections = {"living room": living_room, "bedroom": bedroom}
bedroom.connections = {"kitchen": kitchen, "bathroom": bathroom}
bathroom.connections = {"bedroom": bedroom, "backyard": backyard}
backyard.connections = {"bathroom": bathroom}

# Game initialization
player_name = input("Enter your name: ")
player = Player(player_name)
player.current_room = living_room

print("Welcome to the Text-Based House Navigation Game, {}!".format(player.name))
print("You are now in the", player.current_room.name)
print(player.current_room)
player.current_room.show_items()

# Game loop
while True:
    command = input("Enter your command: ").lower()

    if "go to" in command:
        destination_room = command.split("go to ")[1]
        if destination_room in player.current_room.connections:
            player.current_room = player.current_room.connections[destination_room]
            print("You are now in the", player.current_room.name)
            print(player.current_room)
            player.current_room.show_items()
        else:
            print("You cannot go to that room from here.")

    elif "pick up" in command:
        item = command.split("pick up ")[1]
        player.pick_up_item(item)

    elif "inventory" in command:
        player.show_inventory()

    else:
        print("Invalid command. Please try again.")

    time.sleep(1)

'''
Challenge: Create a Python program that simulates a simple text-based game where the player navigates through different rooms of a house. Each room has specific items to interact with and actions to take, such as picking up objects or using tools. The player can move between rooms by typing commands like "go to [room name]" and can win the game by reaching a final room with a specific item. The game should have a clear set of rules, provide descriptive feedback to the player's actions, and include at least 5 rooms with unique characteristics. Make the game engaging and interactive within the 100-line limit.
'''

# My solution:

import time

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        if len(self.items) > 0:
            print("You see the following items in the room:")
            for item in self.items:
                print("- " + item)
        else:
            print("There are no items in this room.")

    def __str__(self):
        return self.description


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def pick_up_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print("You picked up the", item)
        else:
            print("The item is not in this room.")

    def show_inventory(self):
        if len(self.inventory) > 0:
            print("You are carrying the following items:")
            for item in self.inventory:
                print("- " + item)
        else:
            print("Your inventory is empty.")


# Creating rooms
living_room = Room("Living Room", "A cozy room with a fireplace.", items=["Key"])
kitchen = Room("Kitchen", "A well-equipped kitchen with a dining table.", items=["Knife"])
bedroom = Room("Bedroom", "A spacious bedroom with a king-sized bed.", items=["Flashlight"])
bathroom = Room("Bathroom", "A modern bathroom with a bathtub and shower.", items=["Towel"])
backyard = Room("Backyard", "A lush green backyard with a swing.", items=["Map"])

# Setting room connections
living_room.connections = {"kitchen": kitchen}
kitchen.connections = {"living room": living_room, "bedroom": bedroom}
bedroom.connections = {"kitchen": kitchen, "bathroom": bathroom}
bathroom.connections = {"bedroom": bedroom, "backyard": backyard}
backyard.connections = {"bathroom": bathroom}

# Game initialization
player_name = input("Enter your name: ")
player = Player(player_name)
player.current_room = living_room

print("Welcome to the Text-Based House Navigation Game, {}!".format(player.name))
print("You are now in the", player.current_room.name)
print(player.current_room)
player.current_room.show_items()

# Game loop
while True:
    command = input("Enter your command: ").lower()

    if "go to" in command:
        destination_room = command.split("go to ")[1]
        if destination_room in player.current_room.connections:
            player.current_room = player.current_room.connections[destination_room]
            print("You are now in the", player.current_room.name)
            print(player.current_room)
            player.current_room.show_items()
        else:
            print("You cannot go to that room from here.")

    elif "pick up" in command:
        item = command.split("pick up ")[1]
        player.pick_up_item(item)

    elif "inventory" in command:
        player.show_inventory()

    else:
        print("Invalid command. Please try again.")

    time.sleep(1)
