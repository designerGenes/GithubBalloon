'''
Challenge: 
Create a program that simulates a virtual pet game where users can interact with a digital pet through a series of commands. 
The virtual pet should have attributes such as hunger, happiness, and energy that change based on user actions like feeding, playing, and putting to sleep. 
The program should display the pet's current status and respond to user input accordingly. 
The game should continue until the pet reaches a certain level of satisfaction or energy.
'''

# Define the VirtualPet class with attributes: hunger, happiness, and energy
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
    
    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        self.energy += 5
    
    def play(self):
        self.hunger += 5
        self.happiness += 10
        self.energy -= 10
    
    def sleep(self):
        self.hunger += 5
        self.happiness += 5
        self.energy += 15
    
    def get_status(self):
        return f"{self.name}'s Status - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}"

# Initialize a VirtualPet object
pet = VirtualPet("Pixel")

# Simulate the game loop until the pet reaches a certain level of satisfaction or energy
while pet.happiness > 0 and pet.energy > 0:
    print(pet.get_status())
    action = input("Enter command (feed, play, sleep): ")
    
    if action == 'feed':
        pet.feed()
    elif action == 'play':
        pet.play()
    elif action == 'sleep':
        pet.sleep()

# Game over message
print("Game Over! Your pet is no longer satisfied or has run out of energy.")