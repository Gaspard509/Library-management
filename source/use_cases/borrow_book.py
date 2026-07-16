from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository

class BookOutput:
    def __init__(self, book: Book, message: str):
        self.book = book
        self.message = message

class BorrowBookInput:
    def __init__(self, book_id: int):
        self.book_id = book_id        

class BorrowBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> BookOutput:
        book = self.repository.get_book(book_id)
        if not book:
            return BookOutput(book, "Book not found")
        if not book.is_available():
            return BookOutput(book, "Book is not available")
        book.borrow()
        self.repository.update_book(book)
        return BookOutput(book, "Book borrowed successfully")