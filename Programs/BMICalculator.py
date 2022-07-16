import os

from BMICalcMod import bmiLogic

#Program to Calculate BMI

print("==================================")
print("          BMI Caclulator          ")
print("==================================")
print("")
weight = int(input("Please Enter your Weight in Pounds: "))
height = int(input("Please Enter your Height in Inches: "))
os.system('clear')
bmiLogic(weight, height)

