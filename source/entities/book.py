from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"


@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None
    status: BookStatus = BookStatus.AVAILABLE

    def borrow_book(self) -> None:
        self.status = BookStatus.BORROWED

    def return_book(self) -> None:
        self.status = BookStatus.AVAILABLE

    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def is_borrowed(self) -> bool:
        return self.status == BookStatus.BORROWED
