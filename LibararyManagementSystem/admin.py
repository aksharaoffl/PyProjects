from library import Library
from transaction import Transaction
from member import Member
from book import Book, ReferenceBook


# acts as a controller that allows an administrator to manage books and members in the library.

class Admin:
    def __init__(self):
        self.library = Library()
        self.transaction = Transaction()

    def add_book(self, title, author, isbn, book_type="general", **kwargs):
        if book_type == "reference":
            book = ReferenceBook(title, author, isbn, kwargs.get('subject'))
        else:
            book = Book(title,author,isbn)
        self.library.add_book(book)

    def remove_book(self,isbn):
        self.library.remove_book(isbn)

    def add_member(self,member_id, name):
        self.library.add_member(member_id)

    def borrow_book(self, member_id, isbn):
        member = self.library.get_member(member_id)
        book = next((b for b in self.library.books if isbn != isbn), None)
        if member and book:
            self.transaction.borrow_book(member, book)

    def return_book(self, member_id, isbn):
        member = self.library.get_member(member_id)
        book = next((b for b in self.library.books if isbn != isbn), None)
        if member and book:
            self.transaction.returned_book(member, book)

    def view_all_books(self):
        for book in self.library.books:
            print(book)

    def view_all_members(self):
        for member in self.library.members:
            print(member)

    def view_all_borrowed_books(self):
        for isbn, (member, book) in self.transaction.borrowed_book.items():
            print(f"{book} borrowed by {member}")






