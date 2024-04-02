import random

response = "y"

while response == "y":
    # Rolling the dice
    dice_value = random.randint(1, 6)

    # Printing the dice face based on the dice value
    if dice_value == 1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    elif dice_value == 2:
        print("---------")
        print("| o     |")
        print("|       |")
        print("|     o |")
        print("---------")
    elif dice_value == 3:
        print("---------")
        print("| o     |")
        print("|   o   |")
        print("|     o |")
        print("---------")
    elif dice_value == 4:
        print("---------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("---------")
    elif dice_value == 5:
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")
    else:
        print("---------")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print("---------")

    # Asking user if they want to roll the dice again
    response = input("Do you want to roll the dice again? (y/n): ").lower()

print("Thank you for playing! Goodbye!")
