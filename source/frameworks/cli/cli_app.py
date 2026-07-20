from source.interface_adapters.controllers.book_controller import BookController
from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository


class _C:
    RESET = '\033[0m'
    RED = '\033[31m'
    BOLD = '\033[1m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'


def _banner(text: str) -> None:
    print(f"{_C.BOLD}{_C.CYAN}{text}{_C.RESET}")
    print(f"{_C.BOLD}{_C.YELLOW}{'=' * len(text)}{_C.RESET}")
    print(f"{_C.BOLD}{_C.GREEN}Welcome to the Library Management System!{_C.RESET}\n")


def _ok(message: str) -> None:
    print(f"{_C.BOLD}{_C.GREEN}{message}{_C.RESET}\n")


def _error(message: str) -> None:
    print(f"{_C.BOLD}{_C.RED}{message}{_C.RESET}\n")


def run_cli() -> None:
    repository = InMemoryBookRepository()
    controller = BookController(repository)
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
            output = controller.add_book(title, author)
            _ok(f"Book added: ID={output['id']} {output['title']} by {output['author']}")

        elif cmd == "borrow":
            try:
                book_id = int(input("Enter book ID to borrow: ").strip())
            except ValueError:
                _error("Book ID must be a number.")
                continue
            output = controller.borrow_book(book_id)
            if output["success"]:
                book = output["book"]
                _ok(f"Book borrowed: {book['title']} by {book['author']}")
            else:
                _error(output["message"])

        elif cmd == "return":
            title = input("Enter book title to return: ").strip()
            output = controller.return_book(title)
            if output["success"]:
                book = output["book"]
                _ok(f"Book returned: {book['title']} by {book['author']}")
            else:
                _error(output["message"])

        elif cmd == "list":
            books = controller.list_books()
            if not books:
                print("No books found.")
            else:
                for book in books:
                    status = "Borrowed" if book["is_borrowed"] else "Available"
                    print(f"Book {book['id']}: {book['title']} by {book['author']} ({status})")

        else:
            _error(f"Unknown command: {cmd}")
