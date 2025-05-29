from studmgmtsys import StudentManagementSystem

print("=========================================")
print("Welcome to our student management system!")
print("=========================================\n")

def main():
  studmgmt = StudentManagementSystem()
  while True:
    studmgmt.main_menu()
    option = int(input("Choose what you want to do: "))
    
    if option == 1:
      studmgmt.enroll_student()

    elif option == 2:
      studmgmt.view_student()
        
    elif option == 3:
      studmgmt.update_info()
    
    elif option == 4:
      studmgmt.remove_student()

    elif option == 5:
      print("Exiting the system.......")
      break
    else:
        print("Invalid option. Please choose a valid number.")  

main()
