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
      pass
    
    elif option == 4:
      pass

    elif option == 5:
      print("Exiting the system.......")
      break
    else:
        print("Invalid option. Please choose a valid number.")  

main()
