import os

def checkMenu():
    print("MENU")
    print("====================")
    print("1. Espresso  == ₱65 |")
    print("2. Americano == ₱75 |")
    print("3. Latte     == ₱55 |")
    print("====================")
    input("Press Enter to go back to Main Menu...")  


def order():
    menu = {
        1: ("Espresso", 65),
        2: ("Americano", 75),
        3: ("Latte", 55)
    }

    total = 0

    print("MENU")
    print("====================")
    for key, (item, price) in menu.items():
        print(f"{key}. {item:<10} == ₱{price}")
    print("====================")

    while True:
        try:
            choice = int(input("Enter your order (0 to finish): "))
            
            if choice == 0:  # Exit ordering
                break

            if choice in menu:
                item, price = menu[choice]
                print(f"You ordered {item}")
                total += price
            else:
                print("Error::: Enter a valid number!")

        except ValueError:
            print("Error::: Please enter a number only.")

    print("\nYour total order is: ₱" + str(total))
    input("Press Enter to continue...")


def mainMenu():
    print("=================")
    print("1. Check Menu")
    print("2. Order")
    print("3. Chek Order")
    print("4. Exit")
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
    os.system("cls")
    print("\nWelcome, Customers")
    print("---Coffee Yow!----")
    print("==================")
    mainMenu()
