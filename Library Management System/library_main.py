from library_database import books
from library_service import add_new_book,view_book, update_book_info


print("======================")
print("Welcome to our library!")
print("======================")

while True:
  print("======================")
  print("1. Add a new book")
  print("2. View all the books")
  print("3. Update book info")
  print("4. Remove a book")
  print("5. Exit")
  print("======================")
  option = int(input("Choose what you want to do: "))
  
  if option == 1:
    add_new_book()
  elif option == 2:
    view_book()
  elif option == 3:
    update_book_info()
  elif option == 4:
    pass
  elif option == 5:
    print("Exiting the system.......")
    break
  else:
      print("Invalid option. Please choose a valid number.")  
  

