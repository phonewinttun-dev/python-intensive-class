from db import students
from student_class import Students
from utilities import search_item

class StudentManagementSystem:
  def __init__(self):
    self.students = students

  def main_menu(self):
    print("======================")
    print("1. Enroll a new student")
    print("2. View all the students")
    print("3. Update info")
    print("4. Remove a student")
    print("5. Exit")
    print("======================")

  def enroll_student(self):
    student_id = input("Enter an ID: ")
    name = input("Enter a student name: ")
    while True:
      age = input("Enter age: ")

      if not age.isdigit():
        print("Please enter a digit for age.")
      else:
        int_age = int(age)

        if int_age <= 0:
          print("Error! Please enter a valid age.")
        else:
          break
        
    major = input("Enter a specialized major: ")
    new_student = Students(student_id, name, int_age, major)
    
    self.students.append(new_student)
    print("Enrollment successful!")

  def view_student(self):
      print("======================")
      print("Students' list:")
      print("======================\n")
      for stud in self.students:
        print(f"Name: {stud.name}\t Age: {stud.age}\t Major: {stud.major}")

  def update_info(self):
    student_id = input("Enter ID of the student you want to update: ")
    wanted_student = None
    wanted_student = search_item(student_id, self.students)
    if wanted_student:
      print(f"Current info of the student: {wanted_student.display_info()}")
      name = input(f"Enter new name(leave blank to keep current): ")
      
      while True:
        age = input("Enter age(leave blank to keep current): ")

        if not age.isdigit():
          print("Please enter a digit for age.")
        else:
          int_age = int(age)

          if int_age <= 0:
            print("Error! Please enter a valid age.")
          else:
            break
      major = input(f"Enter new major(leave blank to keep current): ")
    
      if name:
        wanted_student.name = name
    
      if age:
        wanted_student.age = int_age

      if major:
        wanted_student.major = major

    print(f"{wanted_student.name} is updated successfully!")

  def remove_student(self):
    student_id = input("Enter ID of the student you want to remove: ")
    wanted_student = search_item(student_id, self.students)
    self.students.remove(wanted_student)
    print(f"{wanted_student.name} is removed successfully!")
