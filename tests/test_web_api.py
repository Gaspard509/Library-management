import json
import pytest

from source.frameworks.web.flask_app import create_app
from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def repository():
    return InMemoryBookRepository()

class TestAddBookAPI:
    def test_add_book(self, app):
        client = app.test_client()
        response = client.post('/books', json={'title': 'Test Book', 'author': 'Test Author'})
        data = json.loads(response.data)
        assert response.status_code == 201
        assert data['message'] == "Book added successfully"

class TestBorrowBookAPI:
    def test_borrow_book_success(self, app, repository):
        # First, add a book to the repository
        add_book_use_case = AddBook(repository)
        add_book_input = AddBookInput(title="Test Book", author="Test Author")
        add_book_output = add_book_use_case.execute(add_book_input)

        client = app.test_client()
        response = client.post(f'/books/{add_book_output.book.id}/borrow')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['message'] == "Book borrowed successfully"

    def test_borrow_book_not_found(self, app):
        client = app.test_client()
        response = client.post('/books/999/borrow')  # Non-existent book ID
        data = json.loads(response.data)
        assert response.status_code == 400
        assert data['message'] == "Book not found"

class TestReturnBookAPI:
    def test_return_book_success(self, app, repository):
        # First, add a book and borrow it
        add_book_use_case = AddBook(repository)
        add_book_input = AddBookInput(title="Test Book", author="Test Author")
        add_book_output = add_book_use_case.execute(add_book_input)

        borrow_book_use_case = BorrowBook(repository)
        borrow_book_input = BorrowBookInput(book_id=add_book_output.book.id)
        borrow_book_use_case.execute(borrow_book_input)

        client = app.test_client()
        response = client.post(f'/books/{add_book_output.book.title}/return')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['message'] == "Book returned successfully"

    def test_return_book_not_found(self, app):
        client = app.test_client()
        response = client.post('/books/Non-existent Book/return')  # Non-existent book title
        data = json.loads(response.data)
        assert response.status_code == 400
        assert data['message'] == "Book not found"

class TestListBooksAPI:
    def test_list_books(self, app, repository):
        # First, add some books to the repository
        add_book_use_case = AddBook(repository)
        add_book_input1 = AddBookInput(title="Test Book 1", author="Test Author 1")
        add_book_input2 = AddBookInput(title="Test Book 2", author="Test Author 2")
        add_book_use_case.execute(add_book_input1)
        add_book_use_case.execute(add_book_input2)

        client = app.test_client()
        response = client.get('/books')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert len(data) == 2
        assert data[0]['title'] == "Test Book 1"
        assert data[1]['title'] == "Test Book 2"        
