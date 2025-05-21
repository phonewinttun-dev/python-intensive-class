number_one = float(input("Enter a number: "))
number_two = float(input("Enter a number: "))
number_three = float(input("Enter a number: "))

if number_one > number_two and number_one > number_three:
  print(f"{number_one} is the greatest number.")
elif number_one > number_two and number_one > number_three:
  print(f"{number_two} is the greatest number.")
else:
  print(f"{number_three} is the greatest number.")

'''
alternative way to find maximum number

numbers = []

for i in range(3):
  input_number = float(input("Enter a number: "))
  numbers.append(input_number)

max_number = max(numbers)
print(f"{max_number} is the greatest number.")
'''