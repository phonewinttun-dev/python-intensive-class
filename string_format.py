name = input("Enter your name: ")
age = int(input("Enter your age: "))
job = input("Enter your job: ")

# print(f"Your name is {name}, you're {age} years old and you are a {job}")
# alternative way to format string
print("Your name is {}, you're {} years old and you are a {}".format(name, age, job))