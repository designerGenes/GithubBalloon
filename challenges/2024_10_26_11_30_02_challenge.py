'''
Challenge: 
Create a Python program that simulates a vending machine. The program should allow users to select a product, insert coins, and receive change if necessary. The vending machine should have a list of available products with corresponding prices. Users should be able to keep purchasing items until they choose to stop. Display the current balance after each purchase and provide an option for users to request a refund of their remaining balance. The program should handle invalid inputs gracefully and provide appropriate messages to guide the user.

My solution:
'''

class VendingMachine:
    def __init__(self):
        self.products = {"Cola": 1.50, "Chips": 1.00, "Candy": 0.75}
        self.balance = 0

    def display_products(self):
        print("Available products:")
        for product, price in self.products.items():
            print(f"{product}: ${price}")

    def insert_coins(self):
        try:
            coins = float(input("Insert coins ($0.25, $0.50, $1): "))
            if coins in [0.25, 0.50, 1.00]:
                self.balance += coins
            else:
                print("Invalid coin. Please insert $0.25, $0.50, or $1.")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")

    def purchase_product(self, product):
        if product in self.products:
            price = self.products[product]
            if self.balance >= price:
                self.balance -= price
                print(f"Here is your {product}. Remaining balance: ${self.balance}")
            else:
                print("Insufficient balance. Please insert more coins.")
        else:
            print("Invalid product. Please select from the available products.")

    def request_refund(self):
        if self.balance > 0:
            print(f"Refunding ${self.balance}")
            self.balance = 0
        else:
            print("No balance to refund.")

vending_machine = VendingMachine()

while True:
    vending_machine.display_products()
    
    choice = input("Select a product or type 'refund' to request a refund, or 'exit' to stop: ").capitalize()
    
    if choice == 'Refund':
        vending_machine.request_refund()
    elif choice == 'Exit':
        print("Thank you for using the vending machine!")
        break
    else:
        vending_machine.purchase_product(choice)
        print(f"Current balance: ${vending_machine.balance}")
        
    vending_machine.insert_coins()
    print("---------------------------------------------")