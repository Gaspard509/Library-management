import copy
from typing import List, Optional

from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> Book:
        self.books.append(book)
        return book

    def get_book(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.id == book_id:
                return copy.deepcopy(book)
        return None

    def update_book(self, book: Book) -> Book:
        for i, b in enumerate(self.books):
            if b.id == book.id:
                self.books[i] = copy.deepcopy(book)
                return book
        raise ValueError("Book not found")

    def list_books(self) -> List[Book]:
        return copy.deepcopy(self.books)