num = int(input("Enter a number: "))
result = 1
for i in range(1, num + 1):
  result *= i
  
print(f"Factorial of {num} is {result}")

'''
Visualization of the calculation

if user_input == 5

result = 1 * 1 => 1
result = 1 * 2 => 2
result = 2 * 3 => 6
result = 6 * 4 => 24
result = 24 * 5 => 120

'''