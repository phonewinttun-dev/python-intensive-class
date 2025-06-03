from library_database import books
from utilities import search_item
from book_class import Book

'''
class library_management_system:
  def __init__(self):
    self.library = books

  def id_auto_generator(self):
    max_id = 0
    for b in self.books.keys():
      current_id = int(b)
      if current_id > max_id:
            max_id = current_id
    new_id = max_id + 1
    return f"{new_id:d03}"
  

  def add_new_book(self):
    book_id = self.id_auto_generator()
    book_title = input("Enter book title: ")
    author_name = input("Enter author's name: ")
    book_genre = input("Enter genre: ")

    while True:
      book_status = input("Enter book status (Available/Unavailable): ")
      if book_status == "available":
        is_avaialable = True
        break
      elif book_status == "unavailable":
        is_avaialable = False
        break
      else:
        print("Please enter valid status. (Available / Unavailable)")
    
    new_book = Book(book_id, book_title, author_name, book_genre, is_avaialable)

    self.books[book_id] = new_book
    print(f"{new_book.title} has been added successfully")

  def view_book(self):
    print("======================")
    print("Books' list:")
    print("======================\n")
    for book in self.books.values():
      print(book.display_info())

  def update_book_info():
    book_id = int(input("Enter ID of the book you want to update: "))
    wanted_book = None
    wanted_book = search_item(book_id, books)
    if wanted_book:
      print(f"Current info of the book: {wanted_book}")
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

  def remove_book():
    book_id = int(input("Enter ID of the book you want to remove: "))
    wanted_book = search_item(book_id, books)
    if wanted_book:
      books.remove(wanted_book)
      print(f"{wanted_book} is removed successfully!")
    else:
      print("Book not found!")
'''
