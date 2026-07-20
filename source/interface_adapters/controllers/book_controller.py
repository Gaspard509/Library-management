from source.use_cases.interface.interface import BookRepository
from source.interface_adapters.presenters.book_presenter import BookPresenter

from source.use_cases.add_book import AddBook, AddBookInput
from source.use_cases.borrow_book import BorrowBook, BorrowBookInput
from source.use_cases.return_book import ReturnBook, ReturnBookInput
from source.use_cases.list_books import ListBooks


class BookController:
    def __init__(self, repository: BookRepository):
        self.add_book_use_case = AddBook(repository)
        self.borrow_book_use_case = BorrowBook(repository)
        self.return_book_use_case = ReturnBook(repository)
        self.list_books_use_case = ListBooks(repository)

    def add_book(self, title: str, author: str) -> dict:
        input_data = AddBookInput(title, author)
        output = self.add_book_use_case.execute(input_data)
        return BookPresenter.present(output.book)

    def borrow_book(self, book_id: int) -> dict:
        input_data = BorrowBookInput(book_id)
        output = self.borrow_book_use_case.execute(input_data)
        return BookPresenter.present_result(output)

    def return_book(self, title: str) -> dict:
        input_data = ReturnBookInput(title)
        output = self.return_book_use_case.execute(input_data)
        return BookPresenter.present_result(output)

    def list_books(self) -> list:
        output = self.list_books_use_case.execute()
        return BookPresenter.present_list(output.books)
