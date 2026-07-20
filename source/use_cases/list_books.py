from typing import List

from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository


class ListBooksOutput:
    def __init__(self, books: List[Book]):
        self.books = books


class ListBooks:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> ListBooksOutput:
        books = self.repository.find_all()
        return ListBooksOutput(books)
