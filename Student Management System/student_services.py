from student_data import students
from student_class import Students

def search_item(id_to_find, items):
    for item in items:
        if Students.id == id_to_find:
            return item
    else:
        return None

def enroll_student(self):
  student_id = input("Enter an ID: ")
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
  new_student = Students(student_id, name, int_age, major)
  
  self.students.append(new_student)
  print("Enrollment successful!")

def view_student():
    print("======================")
    print("Students' list:")
    print("======================\n")
    for stud in students:
      print(f"Name: {stud.name}\t Age: {stud.age}\t Major: {stud.major}")

def update_info():
  student_id = int(input("Enter ID of the student you want to update: "))
  wanted_student = None
  wanted_student = search_item(student_id, students)
  if wanted_student:
    print(f"Current info of the student: {wanted_student}")
    name = input(f"Enter new name(leave blank to keep current): ")
    age = input(f"Enter new age(leave blank to keep current): ")
    while True:
      age = input("Enter age: ")

      if not age.isdigit():
        print("Please enter a digit for age.")
        continue
      else:
        int_age = int(age)
        break
    major = input(f"Enter new major(leave blank to keep current): ")
  
    if name:
      wanted_student.name = name
  
    if age:
      wanted_student.age = int_age

    if major:
      wanted_student.major = major

  print(f"{wanted_student.name} is updated successfully!")

def remove_student():
   student_id = input("Enter ID of the student you want to remove: ")
   wanted_student = search_item(student_id, students)
   students.remove(wanted_student)
   print(f"{wanted_student.name} is removed successfully!")
