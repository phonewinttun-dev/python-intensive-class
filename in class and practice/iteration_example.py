# python loop -> for loop, while loop
'''
nums = {1, 2, 3, 4, 5}
result = 0

for i in nums:
  result += i

print(result)
'''
"""
for i in range(1,6):
  print("------------")
  for j in range(1,11):
   print(f"{i} x {j} = {i * j}")
"""
result = 'no'

while result in ["no", "impossible"]:
  result = input("Will you be my lover? :").lower()
  if not result in ["no", "impossible"]:
    print("Yayyyy")