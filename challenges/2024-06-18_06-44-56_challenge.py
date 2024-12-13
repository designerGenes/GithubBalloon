Challenge:
Write a Python program to implement a simple text-based adventure game. The game should have at least 3 different rooms or locations the player can explore, each with its own description. 

The player should be able to navigate between rooms by typing in commands like "go north", "go south", "go east", "go west". 

Each room should have interactive elements such as items to pick up, puzzles to solve, or characters to interact with. 

The game should have a win condition, such as finding a specific item or solving a final puzzle, which results in the player "winning" the game.

Your program should be designed to run in the console and can be completed in 100 lines of Python code or less.

My solution: 

```python
class Room:
    def __init__(self, name, description, items=None, directions=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.directions = directions if directions else {}

    def __str__(self):
        return self.name

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

def show_instructions():
    print("Welcome to the Text Adventure Game!")
    print("Commands: go [direction], get [item], look, inventory")

def show_status(player):
    print("You are in the", player.current_room)
    print(player.current_room.description)
    if player.current_room.items:
        print("You see the following items:", [item.name for item in player.current_room.items])
    if player.inventory:
        print("You are carrying:", [item.name for item in player.inventory])

def play_game():
    # Define rooms
    kitchen = Room("Kitchen", "A room with a large stove and fridge.", [Item("key", "An old rusty key")])
    bedroom = Room("Bedroom", "A room with a cozy bed.", [Item("book", "A mysterious book")])
    garden = Room("Garden", "A beautiful garden with colorful flowers.", [Item("flower", "A lovely red rose")])

    kitchen.directions = {'north': garden, 'east': bedroom}
    bedroom.directions = {'west': kitchen}
    garden.directions = {'south': kitchen}

    player = Player(kitchen)

    show_instructions()

    while True:
        show_status(player)
        command = input("Enter your command: ").strip().lower().split()
        verb = command[0]

        if verb == 'go':
            direction = command[1]
            if direction in player.current_room.directions:
                player.current_room = player.current_room.directions[direction]
            else:
                print("You cannot go that way.")

        elif verb == 'get':
            item_name = command[1]
            for item in player.current_room.items:
                if item.name == item_name:
                    player.inventory.append(item)
                    player.current_room.items.remove(item)
                    print("You have picked up the", item.name)
                    break
            else:
                print("That item is not in this room.")

        elif verb == 'look':
            show_status(player)

        elif verb == 'inventory':
            if not player.inventory:
                print("Your inventory is empty.")
            else:
                print("Your inventory contains:", [item.name for item in player.inventory])

        else:
            print("Invalid command. Try again.")

        if len(player.inventory) >= 3:
            print("Congratulations! You have found all the items and won the game.")
            break

play_game()
```