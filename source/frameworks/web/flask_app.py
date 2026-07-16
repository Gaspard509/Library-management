from flask import Flask, request, jsonify

from source.interface_adapters.controllers.book_controller.py import BookController
from source.interface_adapters.repositories.in_memory_book_repository import InMemoryBookRepository

def create_app():
    app = Flask(__name__)
    repository = InMemoryBookRepository()
    book_controller = BookController(repository)

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        output = book_controller.add_book(title, author)
        return jsonify({'message': output.message}), 201

    @app.route('/books/<int:book_id>/borrow', methods=['POST'])
    def borrow_book(book_id):
        output = book_controller.borrow_book(book_id)
        return jsonify({'message': output.message}), 200 if "successfully" in output.message else 400

    @app.route('/books/<string:title>/return', methods=['POST'])
    def return_book(title):
        output = book_controller.return_book(title)
        return jsonify({'message': output.message}), 200 if "successfully" in output.message else 400

    @app.route('/books', methods=['GET'])
    def list_books():
        output = book_controller.list_books()
        books_list = [{'id': book.id, 'title': book.title, 'author': book.author, 'status': "Available" if book.is_available() else "Borrowed"} for book in output.books]
        return jsonify(books_list), 200

    return app
