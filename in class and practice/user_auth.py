username = "PWT"
password = "1735pwt"

input_username = input("Enter username: ")

if input_username == username:
  input_password = input("Enter password: ")
  if input_password == password:
    print("Login Successful!")
  else:
    print("Invalid password")
else:
  print("Invalid username")