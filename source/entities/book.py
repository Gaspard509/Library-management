from dataclasses import dataclass, field
from datetime import date
from enum import Enum  


class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

@dataclass
class Book:

    def __init__(self, title, author, available: BookStatus = BookStatus.AVAILABLE):
        self.title = title
        self.author = author
        self.status = available


    def borrow_book(self) -> None:
        self.status = BookStatus.BORROWED
        
    def return_book(self) -> None:
        self.status = BookStatus.AVAILABLE
        

    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def is_borrowed(self) -> bool:
        return  self.status == BookStatus.BORROWED
        
    