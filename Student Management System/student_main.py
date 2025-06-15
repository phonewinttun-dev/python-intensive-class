from studmgmtsys import StudentManagementSystem
from file_handling import load_data, save_data
from student_class import Students

print("=========================================")
print("Welcome to our student management system!")
print("=========================================\n")


def main():
  students_data = load_data("students_data.txt")
  studmgmt = StudentManagementSystem(students_data)
  while True:
    studmgmt.main_menu()

    option = int(input("Choose what you want to do: "))
    
    if option == 1:
      student_name = input("Enter the name of the student: ")
      while True:
        student_age_input = input("Enter the age of student: ")
        if not student_age_input.isdigit():
          print("Please enter a nnumber.")
          continue
        student_age = int(student_age_input)
        if student_age < 0 or student_age > 100: 
          print("Please enter a valid age.")
        else:
          break
      major = input("Enter the major of the student: ")
      student_id = studmgmt.id_auto_generator()
      new_student = Students(student_id, student_name, student_age, major)
      studmgmt.enroll_student(new_student)
      save_data(studmgmt.students, "students_data.txt")
      print("-----Enrollment Successful!-----")

    elif option == 2:
      studmgmt.view_student()
        
    elif option == 3:
      student_id = input("Enter the ID of the student you want to update:")
      student_name = input("Enter new student name(press Enter to skip): ")
      while True:
        student_age_input = input("Enter new student age(press Enter to skip): ")
        if student_age_input.strip() == "":
          student_age = ""
          break
        if not student_age_input.isdigit():
            print("Please enter a nnumber.")
            continue
        student_age = int(student_age_input)
        if (0 < student_age >= 100): 
            print("Please enter a valid age.")
        else:
          break
      major = input("Enter new student major(press Enter to skip): ")
      updated_student = studmgmt.update_info(student_id, student_name, student_age, major)
      if updated_student:
        print("-----Student Info updated successfully!-----")
        save_data(studmgmt.students, "students_data.txt")
      else:
        print("Student not found! Please enter the ID of existing student!")

    
    elif option == 4:
      pass

    elif option == 5:
      print("Exiting the system.......")
      break
    else:
        print("Invalid option. Please choose a valid number.")  

main()
