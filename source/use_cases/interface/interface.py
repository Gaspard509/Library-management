from abc import ABC, abstractmethod

class BookRepository(ABC):
    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def get_book(self, title):
        ...

    @abstractmethod
    def save(self, book):
        ...