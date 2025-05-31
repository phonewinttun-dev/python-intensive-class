class Book:
    def __init__(self, book_id, title, author, genre, isAvailable):
        self.id = book_id
        self.title =title
        self.author = author
        self.genre = genre
        self.isAvailable = isAvailable

    def display_info(self):
        return (f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Is_Available: {self.isAvailable}")