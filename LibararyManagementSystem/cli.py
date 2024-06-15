from library import Library
from transaction import Transaction
from member import Member
from book import Book, ReferenceBook
from admin import Admin

def main():
    admin = Admin()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View All Books")
        print("8. View All Members")
        print("9. View Borrowed Books")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book_type = input("Enter book type (general/reference): ").lower()
            if book_type == 'reference':
                subject = input("Enter book subject: ")
                admin.add_book(title, author, isbn, book_type=book_type, subject=subject)
            else:
                admin.add_book(title, author, isbn)
            print("Book added successfully.")

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            admin.remove_book(isbn)
            print("Book removed successfully.")

        elif choice == '3':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            admin.add_member(member_id, name)
            print("Member added successfully.")

        elif choice == '4':
            member_id = input("Enter member ID to remove: ")
            admin.remove_member(member_id)
            print("Member removed successfully.")

        elif choice == '5':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to borrow: ")
            admin.borrow_book(member_id, isbn)
            print("Borrow operation completed.")

        elif choice == '6':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to return: ")
            admin.return_book(member_id, isbn)
            print("Return operation completed.")

        elif choice == '7':
            admin.view_all_books()

        elif choice == '8':
            admin.view_all_members()

        elif choice == '9':
            admin.view_borrowed_books()

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
