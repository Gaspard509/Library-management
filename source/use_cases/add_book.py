from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository


class AddBookInput:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class BookOutput:
    def __init__(self, book: Book, message: str):
        self.book = book
        self.message = message


class AddBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, input_data: AddBookInput) -> BookOutput:
        book = Book(input_data.title, input_data.author)
        book = self.repository.save(book)
        return BookOutput(book, "Book added successfully")
