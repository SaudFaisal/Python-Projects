"""
1.import json to save the contact in a json file.
2.import os to add a json file if there isn't any or to check the path.
3.add get_number to avoid ValueError,then we created finddir to find the direction of the file,we used json_path = os.path.join(finddir,"contact_json") ==> to let the var enter the dir and create a json file.
4.we assign json_path to the contact.json we use if with os exith to check whether the file exits or no , and we use os getsize > 0 to check if the file exits and it's not empty.
5.if the condition was True,We usa Try function to avoid if there is any error with the file it's self then, we assign the contact_json = open(json_path, "r") , then we load the info to contact then we close by contact_json.close().
6.if the condition was False,we use contact_json = open(json_path, "w") to create a file called contact.json then close by contact_json.close().
7.use while True for the loop so the code keep on running until the user wants to quit.
8.input choice= options to choose from it.
9.if user choose 1 = add contact we set 3 var name,phone,email then we add them to contact .
10.if user choose 2 = Search Contact we check if contact is empty first then we use if name in contact the print the information and we use len(contact) == 0 to check if there is data or no.
11.if user choose 3 = update contact input the name then check if not in contact = True continue false let user choose if he wants to change phone or email then set the new data to replace old one.
12.if user choose 4 = Delete Contact use for loop with contact.items() to print out the name and the info then we use the same method before to check if the name is there we use dl contact[name].
13.if user choose 5 = show all contacts we use the for loop with the contact.items() to print the info out and we use len(contact) == 0 to check if there is data or no.
14.if user choose 6 = quit print(Goodbye!) and use breack function to quit .
15.if user choose any other number print(That's not an option,Try again.)
16.after the while loop end we use contact_json = open(json_path, "w") to open the file and w is to write the file context then we use json.dump(contact, contact_json) to save the data in the json file and we use contact_json.close() to close the file.
"""

import json
import os

def get_number(text):
    try:
        a = int(input(text))
        return a
    except ValueError:
        print("That's not a number,Try again.")
        return None

contact = {}

finddir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(finddir, "Contact.json")

if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
    try:
        contact_json = open(json_path, "r")
        contact = json.load(contact_json)
        contact_json.close()
    except json.JSONDecodeError:
        print("The file is corrupted,Please fix it manually or it will delete all the contact automatically.")
        contact = {}
else:
    contact_json = open(json_path, "w")
    contact_json.close()

while True:
    choice = get_number("Select which option you want.\n1 - Add contact\n2 - Search Contact\n3 - Update Contact\n4 - Delete Contact\n5 - Show all Contacts\n6 - Quit\nEnter the number here: ")
    if choice is None:
        continue

    if choice == 1:
        name = input("Enter the contact name: ")
        if name in contact:
            print("That name is already in a contact,Please try a different name.")
            continue
        phone = get_number("Enter the contact number: ")
        if phone is None:
            continue
        email = input("Enter contact email: ")

        contact[name] = {'phone': phone ,'email' : email}
    elif choice == 2:
        if len(contact) == 0:
            print("There is no contact to search.")
            continue
        name = input("Enter the contact name: ")
        if name in contact:
            print(f"Name: {name}, phone: {contact[name]['phone']}, email: {contact[name]['email']}")
        else:
            print("There is no contact with that name.")
            continue
    elif choice == 3:
        if len(contact) == 0:
            print("There is no contact to update.")
            continue
        name = input("Enter the contact name: ")
        if name not in contact:
            print("There is no contact with that name.")
            continue
        edit = get_number("Select which option you want to edit.\n1 - Phone\n2 - email\nEnter the number here: ")
        if edit is None:
            continue
        if edit == 1:
            newphone = get_number("Enter the new number here: ")
            if newphone is None:
                continue
            contact[name]['phone'] = newphone
        elif edit == 2:
            newemail = input("Enter the new email here: ")
            contact[name]['email'] = newemail
        else:
            print("That's not an option")
    elif choice == 4:
        if len(contact) == 0:
            print("There is no contact to delete.")
            continue
        for keys , info in contact.items():
            print(f"Name: {keys}, phone: {info['phone']}, email: {info['email']}")
        name = input("Enter the contact name to delete: ")
        if name not in contact:
            print("There is no contact with that name.")
            continue
        del contact[name]
        print(f"the contact {name} has been deleted successfully.")
    elif choice == 5:
        if len(contact) == 0:
            print("There is no contacts.")
            continue
        for keys, info in contact.items():
            print(f"Name: {keys}, phone: {info['phone']}, email: {info['email']}")
    elif choice == 6:
        print("GoodBye!")
        break
    else:
        print("That's not an option,Try again.")

contact_json = open(json_path, "w")
json.dump(contact, contact_json)
contact_json.close()