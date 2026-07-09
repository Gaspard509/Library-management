from source.use_cases.interface import BookRepository
from source.entities.book  import Book

class BookInput:
    def __init__(self, title:str, author:str):
        self.title = title
       

class BookOutput:
    def __init__(self, book:Book, message:str):
        self.book = book
        self.message = message


class ReturnBook:
    def __init__(self, repository:BookRepository):
        self.repository = repository
        
    def execute(self,returnbook:BookInput) -> BookOutput:
        book= self.repository.get_book(repository.title)    
        if not book:
            return BookOutput(book, "Book not found")
        if not book.is_borrowed():
            return BookOutput(book, "Book was not borrowed")
        book.borrow_book()
        book=self.repository.upgrade_book(book)
        return BookOutput(book, "Book returned successfully")
