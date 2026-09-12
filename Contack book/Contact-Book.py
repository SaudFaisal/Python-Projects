def get_number(text):
    try:
        a = int(input(text))
        return a
    except ValueError:
        print("That's not a number,Try again.")
        return None




contact = {}


while True:
    choice = get_number("Select which option you want.\n1 - Add contact\n2 - Search Contact\n3 - Update Contact\n4 - Delete Contact\n5 - Show all Contacts\n6 - Quit\nEnter the number here: ")
    if choice is None:
        continue

    if choice == 1:
        name = input("Enter the contact name: ")
        phone = get_number("Enter the contact number: ")
        if phone is None:
            continue
        email = input("Enter contact email: ")

        contact[name] = {"phone": phone ,"email" : email}
    elif choice == 2:
        for keys , info in contact.items():
            print(f"Keys: {keys}, phone: {info["phone"]}, email: {info["email"]}")
        name = input("Enter the contact name: ")
        if name in contact:
            print(contact[name])
        else:
            print("There is no contact with that name.")
            continue
    elif choice == 3:
        name = input("Enter the contact name: ")
        edit = get_number("Select which option you want to edit.\n1 - Phone\n2 - email\nEnter the number here: ")
        if edit is None:
            continue
        if edit == 1:
            newphone = input("enter the new number here: ")
            contact[name]["phone"] = newphone

