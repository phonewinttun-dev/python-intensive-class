#database configuration

students = [{"ID" : 1,
             "Name" : "PWT",
             "Age" : 20 ,
             "Major" : "Computer Science"},
            {"ID" : 2,
             "Name" : "Kaung",
             "Age" : 20,
             "Major" : "Mathematics"},
            {"ID" : 3,
             "Name" : "Myat",
             "Age" : 20,
             "Major" : "Philosophy"}
]

def search_item(id, items):
    for item in items:
        if item['ID'] == id:
            return item
    else:
        return None

def enroll_student():
  student_id = input("Enter ID of the student: ")
  name = input("Enter a student name: ")
  while True:
    age = input("Enter age: ")

    if not age.isdigit():
      print("Please enter a digit for age.")
      continue
    else:
       int_age = int(age)
       break
      
  major = input("Enter a specialized major: ")
  new_student = {'ID' : student_id,
                 'Name' : name,
                 'Age' : int_age,
                 'Major' : major}
  students.append(new_student)
  print("Enrollment successful!")

def view_student():
    print("======================")
    print("Students' list:")
    print("======================\n")
    for stud in students:
      print(f"Name: {stud["Name"]}\t Age: {stud["Age"]}\t Major: {stud["Major"]}")

def update_info():
  student_id = int(input("Enter ID of the student you want to update: "))
  wanted_student = None
  wanted_student = search_item(student_id, students)
  if wanted_student:
    print(f"Current info of the student: {wanted_student}")
    name = input(f"Enter new name(leave blank to keep current): ")
    age = input(f"Enter new age(leave blank to keep current): ")
    major = input(f"Enter new major(leave blank to keep current): ")
  
    if name:
      wanted_student['Name'] = name
  
    if age:
      wanted_student['Age'] = int(age)

    if major:
      wanted_student['Major'] = major

  print(f"{wanted_student} is updated successfully!")

def remove_student():
   student_id = input("Enter ID of the student you want to remove: ")
   wanted_student = search_item(student_id, students)
   students.remove(wanted_student)
   print(f"{wanted_student} is removed successfully!")

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