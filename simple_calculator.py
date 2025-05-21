number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
  result = number_one + number_two
elif operator == "-":
  if number_one > number_two:
    result = number_one - number_two
  else:
    result = number_two - number_one
elif operator == "*":
  result = number_one * number_two
elif operator == "/":
  if number_two != 0:
    result = number_one / number_two
  else:
    result = "Error! Division by zero."

print(f"Result: {result}")