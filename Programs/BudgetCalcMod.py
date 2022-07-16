# Budget Calculator Functions

def BudgetCalculate(income):
    savings = income * .20
    rent = income * .33
    essentials = income * .33
    nonessentials = income * .14
    print("======================================")
    print("             Your Budget              ")
    print("======================================")
    print("Savings:        " + str(savings))
    print("Rent:           " + str(rent))
    print("Essentials:     " + str(essentials))
    print("NonEssentials:  " + str(nonessentials))
    print("=======================================")