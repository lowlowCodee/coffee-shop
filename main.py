def checkMenu():
    print("MENU")
    print("====================")
    print("1. Espresso  == ₱65 |")
    print("2. Americano == ₱75 |")
    print("3. Latte     == ₱55 |")
    print("====================")
    input("Press Enter to go back to Main Menu...")  # para makita muna bago bumalik


def order():
    print("MENU")
    print("====================")
    print("1. Espresso  == ₱65 |")
    print("2. Americano == ₱75 |")
    print("3. Latte     == ₱55 |")
    print("====================")
    order = int(input("Enter your Order: "))
    print(f"You ordered #{order}")
    input("Press Enter to go back to Main Menu...")  # same pause


def mainMenu():
    print("=================")
    print("1. Check Menu")
    print("2. Order")
    print("3. Exit")
    print("=================")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        checkMenu()
    elif choice == 2:
        order()
    elif choice == 3:
        print("Thank you, come again!")
        exit()
    else:
        print("Invalid choice. Try again.")



while True:
    print("\nWelcome, Customers")
    print("---Coffee Yow!----")
    mainMenu()
