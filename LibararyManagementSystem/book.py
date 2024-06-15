class Book:  # Represents a book in the library with attributes like title, author, ISBN, and availability status.

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isavailable = True

    def __str__(self):
        return f"{self.title},by {self.author}, (ISBN : {self.isbn})"

    def borrow(self):
        if self.isavailable:
            self.isavailable = False
        else:
            print(f"The Book {self.title} is not available")

    def return_book(self):
        self.isavailable = True


class ReferenceBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def __str__(self):
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) [Reference - {self.subject}]")