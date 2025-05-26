from library_database import books

def search_item(id_to_find, items):
    for item in items:
        if item['ID'] == id_to_find:
            return item
    else:
        return None


def add_new_book():
  book_title = input("Enter book title: ")
  author_name = input("Enter author's name: ")
  book_genre = input("Enter genre: ")
  book_status = input("Enter book status (Available/Unavailable): ")
  
  if books:
    max_id = 0
    for book in books:
      if "ID" in book and book["ID"] > max_id:
        max_id = book["ID"]
        book_id = max_id + 1
      else:
        book_id = 1

  new_book = {
    "ID" : book_id,
    "Title" : book_title,
    "Author" : author_name,
    "Genre" : book_genre,
    "Status" : book_status
  }

  books.append(new_book)
  print(f"{new_book['Title']} has been added successfully")

def view_book():
  print("======================")
  print("Books' list:")
  print("======================\n")
  for book in books:
    print(f"ID : {book["ID"]}\t Title: {book["Title"]}\t Author: {book["Author"]}\t Genre: {book["Genre"]}\t Status: {book["Status"]}")

def update_book_info():
  book_id = int(input("Enter ID of the book you want to update: "))
  wanted_book = None
  wanted_book = search_item(book_id, books)
  if wanted_book:
    print(f"Current info of the book: \n{books["ID"]}\t {books["Name"]}\t {books["Author"]}\t {books["Genre"]}\t {books["Status"]}")
    book_title = input("Enter new book's title(leave blank to keep current): ")
    author_name = input("Enter new author's name(leave blank to keep current): ")
    book_genre = input("Enter new genre(leave blank to keep current): ")
    book_status = input("Enter book's new status(leave blank to keep current): ")

    if book_title:
       wanted_book["Title"] = book_title

    if author_name:
       wanted_book["Author"] = author_name

    if book_genre:
       wanted_book["Genre"] = book_genre

    if book_status:
       wanted_book["Status"] = book_status

    else:
       return
    
  print(f"Update successful!")
'''
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
      wanted_student['Name'] = name
  
    if age:
      wanted_student['Age'] = int_age

    if major:
      wanted_student['Major'] = major

  print(f"{wanted_student} is updated successfully!")

'''