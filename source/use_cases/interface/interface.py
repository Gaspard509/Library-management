from abc import ABC, abstractmethod
from typing import List, Optional

from source.entities.book import Book


class BookRepository(ABC):
    @abstractmethod
    def save(self, book: Book) -> Book:
        ...

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        ...

    @abstractmethod
    def find_by_title(self, title: str) -> Optional[Book]:
        ...

    @abstractmethod
    def find_all(self) -> List[Book]:
        ...

    @abstractmethod
    def update(self, book: Book) -> Book:
        ...
