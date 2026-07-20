from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository


class ReturnBookInput:
    def __init__(self, title: str):
        self.title = title


class BookOutput:
    def __init__(self, book: Book, message: str):
        self.book = book
        self.message = message


class ReturnBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, input_data: ReturnBookInput) -> BookOutput:
        book = self.repository.find_by_title(input_data.title)

        if not book:
            return BookOutput(None, "Book not found")

        if not book.is_borrowed():
            return BookOutput(None, "Book was not borrowed")

        book.return_book()
        self.repository.update(book)

        return BookOutput(book, "Book returned successfully")
