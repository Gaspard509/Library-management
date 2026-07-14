from datetime import datetime
from typing import List

from source.entities.book import Book

class BookPresenter:
    @staticmethod
    def present(book: Book) -> dict:
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "is_borrowed": book.is_borrowed(),
            "borrowed_at": book.borrowed_at.strftime("%Y-%m-%d %H:%M:%S") if book.borrowed_at else None
        }

    @staticmethod
    def present_list(books: List[Book]) -> List[dict]:
        return [BookPresenter.present(book) for book in books]
        