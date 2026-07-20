from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository


class BorrowBookInput:
    def __init__(self, book_id: int):
        self.book_id = book_id


class BorrowBookOutput:
    def __init__(self, book: Book, message: str):
        self.book = book
        self.message = message


class BorrowBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, input_data: BorrowBookInput) -> BorrowBookOutput:
        book = self.repository.find_by_id(input_data.book_id)

        if not book:
            return BorrowBookOutput(None, "Book not found")

        if not book.is_available():
            return BorrowBookOutput(None, "Book is not available")

        book.borrow_book()
        self.repository.update(book)

        return BorrowBookOutput(book, "Book borrowed successfully")
