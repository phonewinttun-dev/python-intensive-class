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
      pass

    elif option == 2:
      pass
        
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
