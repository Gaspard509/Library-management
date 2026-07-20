from typing import List, Optional


class BookPresenter:

    @staticmethod
    def present(book) -> dict:
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "is_borrowed": book.is_borrowed(),
        }

    @staticmethod
    def present_list(books: List) -> List[dict]:
        return [BookPresenter.present(book) for book in books]

    @staticmethod
    def present_result(output) -> dict:
        """
        Presents a use-case output that may or may not have succeeded
        (i.e. output.book may be None), without ever touching attributes
        on a None book.
        """
        if output.book is None:
            return {"success": False, "book": None, "message": output.message}

        return {
            "success": True,
            "book": BookPresenter.present(output.book),
            "message": output.message,
        }
