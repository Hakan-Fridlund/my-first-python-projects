contacts = {}

while True:
    print("\n1. Lägg till kontakt")
    print("2. Sök kontakt")
    print("3. Ta bort kontakt")
    print("4. Visa alla")
    print("5. Avsluta")

    choice = input("Menyval: ")

    # menyval 1 lägger till kontakt som innehåller namn och nummer
    if choice == "1":
        name = input("\nNamn:").lower().title()
        nummer = input("Nummer:")
        contacts[name] = nummer
        print("Kontakt:", name, "till-lagd")

    # menyval 2 söker om ett namn finns i "listan" eller ej
    elif choice == "2":
        search = input("\nVilken kontakt söker du efter?:").lower().title()

        if search in contacts:
            number = contacts[search]
            print(search + " " + number)
        else:
            print("\nNamnet hittas ej")

    # menyval 3 ta bort en kontakt
    elif choice == "3":
        name = input("\nVilken kontakt vill du ta bort?:").lower().title()
        if name in contacts:
            contacts.pop(name)
            print("\nKontakt: ", name, "borttagen")
        else:
            print("\nNamnet hittas ej")

    # menyval 4 visa alla
    elif choice == "4":
        print("\n")
        for key in sorted(contacts):
            print(key, contacts[key])

    # menyval 5 avsluta
    elif choice == "5":
        break

    else:
        print("\nFelaktig input")
