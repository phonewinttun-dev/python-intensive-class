def password_strength_checker():

  while True:
    password_input = input("Enter a password: ")
  
    if ' ' in password_input:
      print("Password cannot contain spaces.")
      continue

    if len(password_input) < 8:
      print("Password must be at least 8 characters.")
      continue

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for password in password_input:
      if password.isupper():
        has_uppercase = True
      elif password.islower():
        has_lowercase = True
      elif password.isdigit():
        has_digit = True

    if has_digit and has_lowercase and has_uppercase:
      print("Your password is strong.")
      break

    else:
      if not has_digit:
        print("You need at least one digit.")
      if not has_lowercase:
        print("You need at least one lowercase character.")
      if not has_uppercase:
        print("You need at least one uppercase character.")

password_strength_checker()