#database configuration

students = ["George", "Zac", "Gyin", "Daniel", "Peter", "Tun Tun"]


print("======================")
print("Welcome to our system")
print("======================")

while True:
  print("======================")
  print("1. Enroll a new student")
  print("2. View all the students")
  print("3. Remove a student")
  print("4. Exit")
  print("======================")
  option = int(input("Choose what you want to do: "))
  count = 1

  if option == 1:
    new_student = input("Enter a new student name: ")
    students.append(new_student)
    print(f"{new_student} has been enrolled successfully!")
  elif option == 2:
    print("======================")
    print("Students' list:")
    print("======================\n")
    for student in students:
      print(f"{count} : {student}")
      count += 1
      
  elif option == 3:
    while True:
     removed_student = input("Enter a student name you want to remove: ")
     if removed_student in students:
      students.remove(removed_student)
      print(f"{removed_student} is removed successfully!")
      break
     else:
      print("Please enter a valid student name")


  elif option == 4:
    print("Exiting the system.......")
    break
  else:
      print("Invalid option. Please choose a valid number.")  