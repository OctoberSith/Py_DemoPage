import os
import Programs.BudgetCalcMod as BudgetCalcMod

#Console Application to Determine a Proper Budget Given an Income

print("==========================================================")
print("=                  Budget Calculator                     =")
print("==========================================================")
print("==========================================================")
print("=   Enter Your Monthly Income and a budget is created    =")
print("==========================================================")
print("==========================================================")
input("               Press Enter to Continue                    ")
os.system('clear')

income = float(input("Please enter an income amount: "))
os.system('clear')

BudgetCalcMod.BudgetCalculate(income)
input("Thanks for using this budget calculator! Press Enter to close program")