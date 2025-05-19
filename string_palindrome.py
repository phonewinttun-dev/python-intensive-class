input = input("Enter a string: ")
input = input.lower()  # convert to lowercase
for i in range(len(input) // 2):
  if input[i] != input[-(i + 1)]:
    print("Not a palindrome")
  else:
    print("It's a palindrome")
    break