#database configuration
from student_data import students
from student_services import enroll_student, view_student, update_info, remove_student


print("======================")
print("Welcome to our system")
print("======================")

while True:
  print("======================")
  print("1. Enroll a new student")
  print("2. View all the students")
  print("3. Update info")
  print("4. Remove a student")
  print("5. Exit")
  print("======================")
  option = int(input("Choose what you want to do: "))
  
  if option == 1:
    enroll_student()

  elif option == 2:
    view_student()
      
  elif option == 3:
    update_info()
  
  elif option == 4:
     remove_student()

  elif option == 5:
    print("Exiting the system.......")
    break
  else:
      print("Invalid option. Please choose a valid number.")  

# ID_AUTO_GENERATOR

'''  
    while True:
     removed_student = input("Enter a student name you want to remove: ")
     if removed_student in students:
      students.remove(removed_student)
      print(f"{removed_student} is removed successfully!")
      break
     else:
      print("Please enter a valid student name")
  '''