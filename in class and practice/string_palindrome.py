user_input = input("Enter a string: ")
user_input = input.lower()  # convert to lowercase

'''
for i in range(len(input) // 2):
  if input[i] != input[-(i + 1)]:
    print("Not a palindrome")
  else:
    print("It's a palindrome")
    break
'''
'''
# Check if the string is a palindrome using a loop and boolean variable
is_palindrome = True
for i in range(len(input) // 2):
  if input[i] != input[-(i + 1)]:
    is_palindrome = False
    break

if is_palindrome:
  print("It's a palindrome")
else:
  print("Not a palindrome")
''' 

if user_input == user_input[::-1]:
  print("It's a palindrome")
else: 
  print("Not a palindrome")