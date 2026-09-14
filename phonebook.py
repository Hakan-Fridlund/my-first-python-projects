"""
assignment to create at functional phonebook menu
bad design since no functions and functionality embedded in if/else menu
mostly for trying out dictionary datatypes
"""

contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search")
    print("3. Remove contact")
    print("4. Show all")
    print("5. Exit")

    choice = input("Choice: ")

    # choice 1 adds contact
    if choice == "1":
        name = input("\nName:").lower().title()
        nummer = input("Number:")
        contacts[name] = nummer
        print("Contact:", name, " added")

    # choice 2 looks for a contact in contact-list
    elif choice == "2":
        search = input("\nSearch for: ").lower().title()

        if search in contacts:
            number = contacts[search]
            print(search + " " + number)
        else:
            print("\nNot found")

    # menyval 3 remove contact
    elif choice == "3":
        name = input("\nWhich contact to remove?:").lower().title()
        if name in contacts:
            contacts.pop(name)
            print("\nContact: ", name, "removed")
        else:
            print("\nContact not found")

    # menyval 4 Show all
    elif choice == "4":
        print("\n")
        for key in sorted(contacts):
            print(key, contacts[key])

    # menyval 5 exit
    elif choice == "5":
        break

    else:
        print("\nFaulty input")
