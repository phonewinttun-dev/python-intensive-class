number_list = [1, 3, 5, 8, 10, 4, 2, 9]
# even_list = []
# odd_list = []

#find maximum number

max_num = 0

for num in number_list:
  if num > max_num:
    max_num = num
    
print(max_num)

''''
for num in number_list:
  if num % 2 == 0:
    even_list.append(num)
  else:
    odd_list.append(num)

print(even_list)
print(odd_list)
'''
'''
if number_list % 2 == 0:
  even_list.append()
  print(even_list)
else: 
  odd_list.append()
  print(odd_list)
'''