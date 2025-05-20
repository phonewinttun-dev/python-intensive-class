while True:
  password_input = input("Enter a password: ")
  
  if len(password_input) >= 6 and password_input.isalnum():
    print("Strong password.")
    break
  else:
    print("Password must be at least six characters.")