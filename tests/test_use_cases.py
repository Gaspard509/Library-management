import pytest

from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository
from source.use_cases.borrow_book import BorrowBook, BorrowBookInput
from source.use_cases.return_book import ReturnBook, returnBookInput
from source.use_cases.add_book import AddBook, AddBookInput
from source.use_cases.list_books import ListBooks, ListBooksOutput
from soource.entities.book import BookStatus


@pytesr.fixture
    def repository():
    return InMemoryBookRepository()

class TestBorrowBook:
    def test_borrow_book_success(self, repository):
        add_book_use_case = AddBook(repository)
        add_book_input = AddBookInput(title="Test Book", author="Test Author")
        add_book_output = add_book_use_case.execute(add_book_input)

        borrow_book_use_case = BorrowBook(repository)
        borrow_book_input = BorrowBookInput(book_id=add_book_output.book.id)
        borrow_book_output = borrow_book_use_case.execute(borrow_book_input)

        assert borrow_book_output.message == "Book borrowed successfully"
        assert borrow_book_output.book.status == BookStatus.BORROWED

    def test_borrow_book_not_found(self, repository):
        borrow_book_use_case = BorrowBook(repository)
        borrow_book_input = BorrowBookInput(book_id=999)  # Non-existent book ID
        borrow_book_output = borrow_book_use_case.execute(borrow_book_input)

        assert borrow_book_output.message == "Book not found"

class TestReturnBook:
    def test_return_book_success(self, repository):
        add_book_use_case = AddBook(repository)
        add_book_input = AddBookInput(title="Test Book", author="Test Author")
        add_book_output = add_book_use_case.execute(add_book_input)

        borrow_book_use_case = BorrowBook(repository)
        borrow_book_input = BorrowBookInput(book_id=add_book_output.book.id)
        borrow_book_use_case.execute(borrow_book_input)

        return_book_use_case = ReturnBook(repository)
        return_book_input = returnBookInput(title="Test Book")
        return_book_output = return_book_use_case.execute(return_book_input)

        assert return_book_output.message == "Book returned successfully"
        assert return_book_output.book.status == BookStatus.AVAILABLE

    def test_return_book_not_found(self, repository):
        return_book_use_case = ReturnBook(repository)
        return_book_input = returnBookInput(title="Non-existent Book")
        return_book_output = return_book_use_case.execute(return_book_input)

        assert return_book_output.message == "Book not found"        

class TestListBooks:
    def test_list_books(self, repository):
        add_book_use_case = AddBook(repository)
        add_book_input1 = AddBookInput(title="Test Book 1", author="Test Author 1")
        add_book_input2 = AddBookInput(title="Test Book 2", author="Test Author 2")
        add_book_use_case.execute(add_book_input1)
        add_book_use_case.execute(add_book_input2)

        list_books_use_case = ListBooks(repository)
        list_books_output = list_books_use_case.execute()

        assert len(list_books_output.books) == 2
        assert list_books_output.books[0].title == "Test Book 1"
        assert list_books_output.books[1].title == "Test Book 2"

class TestAddBook:
    def test_add_book(self, repository):
        add_book_use_case = AddBook(repository)
        add_book_input = AddBookInput(title="New Book", author="New Author")
        add_book_output = add_book_use_case.execute(add_book_input)

        assert add_book_output.message == "Book added successfully"
        assert add_book_output.book.title == "New Book"
        assert add_book_output.book.author == "New Author"
        assert add_book_output.book.status == BookStatus.AVAILABLE