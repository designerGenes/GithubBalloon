Challenge:
Write a Python program to implement a basic contact management system. The program should have the following functionality:
- Add a new contact with a name, phone number, and email address.
- Update an existing contact's phone number or email address.
- Delete a contact based on their name.
- Display all contacts in the system.
- Search for a contact by name and display their details.
- Save the contacts to a file and load them back when the program starts.
You can use dictionaries or lists to store the contacts, and input/output can be handled through the console. Your program should be concise and easy to understand, fitting within 100 lines of code.

My solution:
```python
import json

contacts = {}

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            global contacts
            contacts = json.load(file)
    except FileNotFoundError:
        pass

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    print("Contact added successfully.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        save_contacts()
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_all_contacts():
    print("All contacts:")
    for name, contact in contacts.items():
        print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Contact not found.")

# Main program
load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_all_contacts()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

```
This solution uses a dictionary to store contacts and provides functions to add, update, delete, display, search contacts, as well as save and load contacts from a JSON file. The main program loop allows users to interact with the contact management system through the console.