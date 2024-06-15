from admin import Admin


def main():
    admin = Admin()

    # Add some books
    admin.add_book("Python Programming", "John Doe", "1234567890")
    admin.add_book("Data Structures", "Jane Smith", "0987654321")
    admin.add_book("Advanced Python", "Steve Jobs", "1122334455", book_type="reference", subject="Programming")

    # Add some members
    admin.add_member("1", "Alice")
    admin.add_member("2", "Bob")

