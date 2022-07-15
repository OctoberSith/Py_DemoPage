import os
import csv

#CSV Demo Playground

file = open('./data/heroes.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

print("Header Columns")
os.system('clear')
print(header)
input("Press Enter")


print("Row Data")
os.system('clear')
rows = []
for row in csvreader:
    print(row)
input("Press Enter")