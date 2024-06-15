# Manages the collection of books, members, and handles operations like adding or removing books and members.

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Added book : {book}")

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.ispn != isbn]
        print(f"Removed book with ISBN {isbn}")

    def search_book(self, title= None, author=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower()):
                results.append(book)
        return results

    def add_member(self,member):
        self.members.append(member)
        print(f"{member} got added")

    def remove_member(self,member_id):
        self.members = [member for member in self.members if member.member_id != member]
        print(f"Member with member id : {member_id} got removed")

    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None