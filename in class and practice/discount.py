'''
amount = float(input("Enter total amount: "))
print(f"Total amount is {amount} \n You need to pay {amount - (amount * 0.1)}")
'''


total_amount = float(input("Enter total amount: "))
age = int(input("Enter age: "))

if age <= 5:
  actual_amt = total_amount * 0.5 
elif age <= 8:
  actual_amt = total_amount * 0.7
elif age <= 12:
  actual_amt = total_amount * 0.9
else:
  actual_amt = total_amount

print(f"Actual amount: {actual_amt}")