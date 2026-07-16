import pytest
from source.entities.book import Book, BookStatus

class TestBook:
    def test_book_initialization(self):
        book = Book("123", "Sample Book", "Author Name")
        assert book.isbn == "123"
        assert book.title == "Sample Book"
        assert book.author == "Author Name"
        assert book.status == BookStatus.AVAILABLE

    def test_book_status_change(self):
        book = Book("123", "Sample Book", "Author Name")
        book.change_status(BookStatus.BORROWED)
        assert book.status == BookStatus.BORROWED

    def test_book_initialization(self):
        book = Book("123", "Sample Book", "Author Name")
        assert book.isbn == "123"
        assert book.title == "Sample Book"
        assert book.author == "Author Name"
        assert book.status == BookStatus.AVAILABLE

    def test_book_status_change(self):
        book = Book("123", "Sample Book", "Author Name")
        book.change_status(BookStatus.BORROWED)
        assert book.status == BookStatus.BORROWED


class TestBookStateTransitions:
    def test_borrow_book(self):
        book = Book("123", "Sample Book", "Author Name")
        book.borrow_book()
        assert book.status == BookStatus.BORROWED

    def test_return_book(self):
        book = Book("123", "Sample Book", "Author Name")
        book.borrow_book()
        book.return_book()
        assert book.status == BookStatus.AVAILABLE

