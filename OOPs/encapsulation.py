# process of bundling attributes and methods together in a single unit to so the specific task
class Book:
    def __init__(self, title, author, isbn, copies):
        self._title = title  # protected attributes
        self._author = author
        self._isbn = isbn
        self._copies = copies

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_isbn(self):
        return self._isbn

    def get_copies(self):
        return self._copies

    def set_copies(self, count):
        if count >= 0:
            self._copies = count
        else:
            print("Copies cannot be negative")

    def _validate_isbn(self, isbn):
        return len(isbn) in [10, 13]


class Library:
    def __init__(self):
        self.__books = {}

    def add_book(self, book):
        if book._validate_isbn(book.get_isbn()):
            self.__books[book.get_isbn()] = book
            print(f"Book '{book.get_title()}' added to the library")
        else:
            print("Invalid ISBN,Book cant be added")

    def remove_book(self, isbn):
        if isbn in self.__books:
            removed_book = self.__books.pop(isbn)
            print(f"Book '{removed_book.get_title()}' removed from the library'")
        else:
            print("Book with given ISBN not found in the library")

    def search_by_title(self, title):
        results = []
        for book in self.__books.values():
            if title.lower() in book.get_title().lower():
                results.append(book)
        return results

    def search_by_author(self, author):
        results = []
        for book in self.__books.values():
            if author.lower() in book.get_author().lower():
                results.append(book)
        return results

    def borrow_book(self, isbn):
        if isbn in self.__books:
            book = self.__books[isbn]
            if book.get_copies() > 0:
                book.set_copies(book.get_copies() - 1)
                print(f"Borrowed '{book.get_title()}.")
            else:
                print(f"No available copies of {book.get_title()}")
        else:
            print("Book with given ISPN not fount in the library")

    def return_book(self, isbn):
        if isbn in self.__books:
            book = self.__books[isbn]
            book.set_copies(book.get_copies() + 1)
            print(f"Returned book {book.get_title()}")
        else:
            print("book with given ispn not found in the library")


book1 = Book("Dalaric", "ARKHN", "1234678910", 15)
book2 = Book("Atomic Habits", "James Clear", "9876541819", 11)
book3 = Book("Hunting Adaline", "H.D.Carlton", "1122334488", 10)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("lets search for the book")
for book in library.search_by_author("ARKHN"):
    print(book.get_title(), book1.get_author(), book1.get_copies())

library.borrow_book("1122334488")

library.return_book("1122334488")
