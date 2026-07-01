class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


    def borrow(self):
        if self.available:
            self.available = False
            return True

        return False


    def return_book(self):
        self.available = True