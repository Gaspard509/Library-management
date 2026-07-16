from typing import List, Optional
from source.use_cases.interface.interface import BookRepository
from source.entities.book import Book
from source.interface_adapters.presenters.book_presenter import BookPresenter

from source.use_cases.add_book import AddBook, AddBookInput, BookOutput
from source.use_cases.interface.interface import BookRepository
from source.use_cases.borrow_book import BorrowBook, BorrowBookInput
from source.use_cases.return_book import ReturnBook, ReturnBookInput
from source.use_cases.list_books import ListBooks, ListBooksOutput



class BookController:
    def __init__(self, repository: BookRepository):
        self.add_book_use_case = AddBook(repository)
        self.borrow_book_use_case = BorrowBook(repository)
        self.return_book_use_case = ReturnBook(repository)
        self.list_books_use_case = ListBooks(repository)

    def add_book(self, title: str, author: str) -> BookOutput:
        use_case = AddBook.execute(AddBookInput(title, author))
        input_data = AddBookInput(title, author)
        return BookPresenter.present(input_data)

    def borrow_book(self, book_id: int) -> BookOutput:
        use_case = BorrowBook.execute(BorrowBookInput(book_id))
        return BookPresenter.present(use_case)

    def return_book(self, title: str) -> BookOutput:
        use_case = ReturnBook.execute(ReturnBookInput(title))
        return BookPresenter.present(use_case)

    def list_books(self) -> ListBooksOutput:
        use_case = ListBooks.execute()
        return BookPresenter.present(use_case)