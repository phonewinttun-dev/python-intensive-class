from book_class import Book

books = [
  { "ID" : "001",
    "Title" : "The Trial",
    "Author" : "Franz Kafka",
    "Genre" : "Fiction",
    "Is_Available" : True
   },
   {
    "ID" : "002",
    "Title" : "မမ",
    "Author" : "မြသန်းတင့်",
    "Genre" : "Fiction",
    "Is_Available" : True
   },
   {
     "ID" : "003",
     "Title" : "The Prince",
     "Author" : "Niccolo Machiavelli",
     "Genre" : "Non-fiction",
     "Is_Available" : False
   },
   {
     "ID" : "004",
     "Title" : "Shock By Shock",
     "Author" : "Dean Young",
     "Genre" : "Poetry",
     "Is_Available" : False
   }
]

book_collection = {} #dictionary to store Book objects

for b in books:
  book_id = b["ID"]
  title = b["Title"]
  author = b["Author"]
  genre = b["Genre"]
  is_available = b["Is_Available"]

  new_book_added = Book(book_id, title, author, genre, is_available)

  book_collection[book_id] = new_book_added

'''
Checking if correct
print(f"Total books in collection: {len(book_collection)}")

book_one = book_collection[1]
print(f"Accessed book ID 1: {book_one.title}")
print(book_one.display_info())
'''

