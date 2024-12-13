Challenge:
Create a Python program that simulates a simple text-based adventure game. The game should include at least three different rooms that the player can navigate through. Each room should have its own description and possible actions the player can take, such as picking up an item, opening a door, or solving a puzzle. The player should be able to move from one room to another based on their actions. Include a win condition that the player must achieve to "complete" the game. The game should provide clear instructions and feedback to the player at each step. Aim to keep the entire program under 100 lines of Python code.

My solution:
```python
def main():
    current_room = "room1"
    win_condition = False

    rooms = {
        "room1": {
            "description": "You are in a dark room with a door to the north.",
            "actions": ["north", "help"],
            "message": "You found a key! It might be useful.",
            "next_room": "room2",
            "key_required": False
        },
        "room2": {
            "description": "You are in a room with a chest. There are doors to the north and east.",
            "actions": ["north", "east", "open chest", "help"],
            "message": "You found a treasure! Good job.",
            "next_room": "room3",
            "key_required": True
        },
        "room3": {
            "description": "You are in a brightly lit room with a door to the south.",
            "actions": ["south", "help"],
            "message": "You unlocked the final door! Congratulations, you won the game!",
            "next_room": "",
            "key_required": False
        }
    }

    while not win_condition:
        print(rooms[current_room]["description"])
        player_action = input("What would you like to do? ").lower()

        if player_action in rooms[current_room]["actions"]:
            if player_action == "help":
                print("Available actions:", rooms[current_room]["actions"])
            elif player_action == "open chest" and current_room == "room2":
                if rooms[current_room]["key_required"]:
                    print("The chest is locked. You need a key to open it.")
                else:
                    print(rooms[current_room]["message"])
                    current_room = rooms[current_room]["next_room"]
            else:
                print(rooms[current_room]["message"])
                current_room = rooms[current_room]["next_room"]
        else:
            print("Invalid action. Type 'help' to see available actions.")

        if current_room == "":
            win_condition = True

if __name__ == "__main__":
    main()
```
This Python program creates a text-based adventure game with three rooms where the player can navigate through by taking appropriate actions. The player must open a chest in the second room to win the game. The program provides instructions and feedback to the player at each step.