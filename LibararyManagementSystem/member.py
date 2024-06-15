from book import Book


class Member:  # Represents a library member with attributes like member ID, name, and borrowed books.

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.isavailable:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name}borrowed {book.title}")
        else:
            print(f"The {book.title} is not available")

    def returned_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} didn't borrow {book.title}")

    def __str__(self):
        return f"Member ID : {self.member_id}, Name : {self.name}"


