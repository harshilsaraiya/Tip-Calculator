print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?5,10,12,15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip= (bill * (tip / 100) / people) * people + bill
print(bill_with_tip)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?5,10,12,15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip= bill *(1+ tip/100)
print(round(bill_with_tip,2))

