print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?5,10,12,15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip= (bill * (tip / 100) / people) * people + bill
rounded_amount=round(bill_with_tip,2)
final= bill_with_tip / people
print(f"The total amount would be {rounded_amount}\n Each person would pay: ${final}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?5,10,12,15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip= bill *(1+ tip/100)
rounded_amount=round(bill_with_tip,2)
final= bill_with_tip / people
print(f"the total bill would be {rounded_amount}\n Each person would pay: ${final}")
