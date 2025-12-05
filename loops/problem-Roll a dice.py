"""
Write a program to simulate a roll of a die/dice.
A die has 6 faces with the number 1 to 6 written on them.
The program should randomly print a number from 1 to 6.
"""
import random
print("Welcome to the game of rolling a dice")
dice_number = [1,2,3,4,5,6]
while True:
    data = input("Press 's' key to roll a dice and 'q' to quite the game: ")
    data = data.strip() # This will remove the invalid space from the input.
    if data == "q":
        print("Thank You for your time.")
        break;
    elif data == "s":
        print(f"Dice Number is: {random.choice(dice_number)}")
    else:
        print("Invalid Input.")
print("Game Ended!")