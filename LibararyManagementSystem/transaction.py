class Transaction:
    def __init__(self):
        self.borrowed_book = {}

    def borrow_book(self, member, book):
        if book.isavailable:
            member.borrow_book()
            self.borrowed_book[book.isbn] = (member, book)
        else:
            print(f"Book is not available")

    def returned_book(self, book, member):
        if book.isbn in self.borrowed_book:
            member.returned_book()
            del self.borrowed_book[book.isbn]
        else:
            print(f"No record of '{book}'being borrowed")
