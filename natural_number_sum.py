natural_number = int(input("Enter a natural number: "))

result = 0

for i in range(1, natural_number + 1):
  result += i

print(result)

'''
Visualization of the calculation

if user_input == 5

result = 0 + 1 => 1
result = 1 + 2 => 3
result = 3 + 3 => 6
result = 6 + 4 => 10
result = 10 + 5 => 15

'''