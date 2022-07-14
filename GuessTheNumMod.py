#Game Logic
import random
import os

def IsNumber (number, userInput):
    if (userInput == number):
        print("You Guessed The Number! Thanks For Playing")
        endInput = input("Press Enter to Exit")
        return
    elif (userInput > number):
        print("The number is lower than the number")
        userInput2 = int(input("Please Next Guess: "))
        os.system('clear')
        if(userInput2 == number):
            print("You Guessed The Number! Thanks For Playing")
            endInput = input("Press Enter to Exit")
            return
        elif(userInput2 > number):
            print("The number is lower than the number")
            userInput3 = int(input("Please Last Guess: "))
            os.system('clear')
            if(userInput3 == number):
                print("You Guessed The Number! Thanks For Playing")
                endInput = input("Press Enter to Exit")
                return
            else:
                print("You did not guess the Number")
                print("The Number was " + str(number))
        elif(userInput2 < number):
            print("The number is higher than the number")
            userInput3 = int(input("Please Enter Last Guess: "))
            os.system('clear')
            if(userInput3 == number):
                print("You Guessed The Number! Thanks For Playing")
                endInput = input("Press Enter to Exit")
                return
            else:
                print("You did not guess the Number")
                print("The Number was " + str(number))
                endInput = input("Press Enter to Exit")
                return
    elif (userInput < number):
        print("The number is higher than the number")
        userInput2 = int(input("Please Next Guess: "))
        os.system('clear')
        if(userInput2 == number):
            print("You Guessed The Number! Thanks For Playing")
            endInput = input("Press Enter to Exit")
            return
        elif(userInput2 > number):
            print("The number is lower than the number")
            userInput3 = int(input("Please Enter Last Guess: "))
            os.system('clear')
            if(userInput3 == number):
                print("You Guessed The Number! Thanks For Playing")
                endInput = input("Press Enter to Exit")
                return
            else:
                print("You did not guess the Number")
                print("The Number was " + str(number))
                endInput = input("Press Enter to Exit")
                return
        elif(userInput2 < number):
            print("The number is higher than the number")
            userInput3 = int(input("Please Enter Last Guess: "))
            os.system('clear')
            if(userInput3 == number):
                print("You Guessed The Number! Thanks For Playing")
                endInput = input("Press Enter to Exit")
                return
            else:
                print("You did not guess the Number")
                print("The Number was " + str(number))
                endInput = input("Press Enter to Exit")
                return



def GameLogic ():
    number = random.randint(1,10)
    print("================================")
    print(" Pick a Number Between 1 and 10 ")
    print("================================")
    userInput = int(input("Enter Guess: "))
    IsNumber(number, userInput)