'''

width = input("Width: ")
length = input("Length: ")
int_width = int(width)
int_length = int(length)
area = int_length * int_width
print("Area: ", area)

'''

'''

name = input("Enter name: ")
age = input("Enter date of birth: ")
int_age = int(age)
print("Your name is", name + age)
print("Your age is",2025 - int_age)

'''

'''

name = input("Enter name: ")
date_of_birth = input("Enter date of birth: ")
occupation = input("Enter occupation: ")
print("Your name:", name , "\n" , "Age:", 2025 - int(date_of_birth), "\n", "Occupation:", occupation)

'''

'''

name = input("Hello, what's your name? \n")
print(f"Hello,{name}!")
date_of_birth = int(input("Please tell us your date of birth: "))
address = input("Where do you live? \n")
occupation = input("What is your occupation? \n")
hobby = input("What is your hobby? \n")

print("\nPersonal information")
print("______________________")
print(f"Name: {name}")
print(f"Age: {2025 - date_of_birth}")
print(f"Address: {address}")
print(f"Occupation: {occupation}")
print(f"Hobby: {hobby}")

'''
'''
num = input("Enter a number: ")
print(num * 3)

'''

num1 = float(input("Enter a num: "))
num2 = float(input("Enter a num: "))

if num1 > num2:
  print(f"{num1} is greater than {num2}")
else:
  print(f"{num2} is greater than {num1}")
