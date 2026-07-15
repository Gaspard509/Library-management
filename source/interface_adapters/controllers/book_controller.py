from typing import List, Optional

from source.use_cases.add_book import AddBook, AddBookInput, BookOutput
from source.use_cases.interface.interface import BookRepository
from source.use_cases.borrow_book import BorrowBook, BorrowBookInput
from source.use_cases.return_book import ReturnBook, ReturnBookInput
from source.use_cases.list_books import ListBooks, ListBooksOutput



class BookController(Controller):
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, title: str, author: str) -> BookOutput:
        use_case = AddBook(self.repository)
        input_data = AddBookInput(title, author)
        return use_case.execute(input_data)

    def borrow_book(self, book_id: int) -> BookOutput:
        use_case = BorrowBook(self.repository)
        input_data = BorrowBookInput(book_id)
        return use_case.execute(input_data)

    def return_book(self, title: str) -> BookOutput:
        use_case = ReturnBook(self.repository)
        input_data = ReturnBookInput(title)
        return use_case.execute(input_data)

    def list_books(self) -> ListBooksOutput:
        use_case = ListBooks(self.repository)
        return use_case.execute()
        