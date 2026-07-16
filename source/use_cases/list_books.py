from source.use_cases.interface.interface import BookRepository

class ListBooksOutput:
    def __init__(self, books):
        self.books = books


class ListBooks:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> ListBooksOuput:
        books = self.repository.get_all()
        return ListBooksOuput(books)
    