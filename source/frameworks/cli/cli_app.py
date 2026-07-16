from source.interface_adapters.controllers.book_controller import BookController
from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository
from source.interface_adapters.controllers.book_controller import BookController

class _C:
         RESET = '\033[0m'
         RED = '\033[31m'  
         BOLD = '\033[1m'
         YELLOW = '\033[33m'
         CYAN = '\033[36m'
         GREEN = '\033[32m'


def _banner(text: str) ->None:
    print(f"{_C.BOLD}{_C.CYAN}{text}{_C.RESET}")
    print(f"{_C.BOLD}{_C.YELLOW}{'=' * len(text)}{_C.RESET}")
    print(f"{_C.BOLD}{_C.GREEN}Welcome to the Library Management System!{_C.RESET}\n") 

def _ok(message: str) -> None:
    print(f"{_C.BOLD}{_C.GREEN}{message}{_C.RESET}\n")

def _error(message: str) -> None:
    print(f"{_C.BOLD}{_C.RED}{message}{_C.RESET}\n")

def run_cli() -> None:
    _banner("Library Management System")
    print("Commands: add | borrow | return | list | exit")

    while True:
        try:
             cmd = input(f"{_C.BOLD}{_C.CYAN}Enter command: {_C.RESET}").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

        if cmd in ("exit", "quit"):
            print("Exiting...")
            break

        elif cmd == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            output = BookController.add_book(title, author)
            _ok(f"Book added: {output.book.title} by {output.book.author}")

        elif cmd == "borrow":
            book_id = int(input("Enter book ID to borrow: ").strip())
            output = BookController.borrow_book(book_id)
            if output.book:
                _ok(f"Book borrowed: {output.book.title} by {output.book.author}")
            else:
                _error(output.message)

        elif cmd == "return":
            title = input("Enter book title to return: ").strip()
            output = BookController().return_book(title)
            if output.book:
                _ok(f"Book returned: {output.book.title} by {output.book.author}")
            else:
                _error(output.message)

        elif cmd == "list":
            output = BookController().list_books()
            if output.books:
                print(f"{_C.BOLD}{_C.CYAN}Books in Library:{_C.RESET}")
                for book in output.books:
                    status = "Available" if book.is_available() else "Borrowed"
                    print(f"- {book.title} by {book.author} [{status}]")
            else:
                _ok("No books in the library.")                    

             


