from source.interface_adapters.controllers.book_controller import BookController
from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository
from source.interface_adapters.controllers.book_controller import BookController

class CLIApp:
    def __init__(self):
        self.repository = InMemoryBookRepository()
        self.book_controller = BookController(self.repository)

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. List Books")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                output = self.book_controller.add_book(title, author)
                print(output.message)
            elif choice == '2':
                book_id = int(input("Enter book ID to borrow: "))
                output = self.book_controller.borrow_book(book_id)
                print(output.message)
            elif choice == '3':
                title = input("Enter book title to return: ")
                output = self.book_controller.return_book(title)
                print(output.message)
            elif choice == '4':
                output = self.book_controller.list_books()
                for book in output.books:
                    status = "Available" if book.is_available() else "Borrowed"
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {status}")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")