import os
import Programs.TempConvertMod as TempConvertMod

#Asks for User Input then Returns Temperature
print("**************************************************")
print("***[Welcome to the Temperature Convert Program]***")
print("**************************************************")
print("**************************************************")
print("*Please Enter a 1 for Celsius or 2 for Fahrenheit*")
print("**************************************************")
print("             Press Enter to Start                 ")
print("**************************************************")
input()
os.system('clear')
choice = int((input("Please Enter 1 or 2: ")))
os.system('clear')
if choice == 1:
    tempF = float(input("Please Enter a Celsius Temperature: "))
    os.system('clear')
    print("Your Fahrenheit Temperature is: " + str(TempConvertMod.convertCelsius(tempF)))
    print("Thanks For Using Temperature Converter")
elif choice == 2:
    tempC = float(input("Please Enter a Fahrenheit Temperature: "))
    os.system('clear')
    print("Your Celsius Temperature is: " + str(TempConvertMod.convertCelsius(tempC)))
    print("Thanks For Using Temperature Converter")
else:
    os.system('clear')
    print("You have chosen an invalid choice. Please Restart")
    print("Thanks For Using Temperature Converter")
