from typing import List, Optional

from source.entities.book import Book
from source.use_cases.interface.interface import BookRepository


class InMemoryBookRepository(BookRepository):

    def __init__(self):
        self.books: List[Book] = []
        self.next_id = 1

    def save(self, book: Book) -> Book:
        book.id = self.next_id
        self.next_id += 1
        self.books.append(book)
        return book

    def find_by_id(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_all(self) -> List[Book]:
        return self.books

    def update(self, book: Book) -> Book:
        # Objects are stored by reference in this in-memory list, so the
        # entity is already mutated in place. This method exists to satisfy
        # the BookRepository port and to make the persistence step explicit.
        return book
