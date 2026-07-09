from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository



class AddBookInput:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookOutput:
    def __init__(self, book: Book, message:str):
        self.book = book
        self.message = message

class AddBook:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, inputbook: AddBookInput) -> BookOutput:
        book = Book(inputbook.title, inputbook.author)
        book=self.repository.save(book)

        return BookOutput(book)
