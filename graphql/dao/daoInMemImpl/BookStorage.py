from entities.Book import Book
from typing import List

# books = [
#             Book(id = "Book-1", name="Life", pageCount=10, authorName="Udit"),
#             Book(id = "Book-2", name="Sea", pageCount=10, authorName="Sandeep"),
#             Book(id = "Book-3", name="Land", pageCount=10, authorName="Kanishk"),
#             Book(id = "Book-4", name="Life-2", pageCount=10, authorName="Udit")
#         ]

# def getById(id: str) -> Book:
#     listBook = list(filter(lambda book: book.id == id, books))
#     return listBook[0]

# def getBookByAuthor(authorName: str) -> List[Book]:
#     return list(filter(lambda book : book.authorName == authorName, books))

# def getBookByAuthorAndId(authorName: str, bookId: str) -> List[Book]:
#     return list(filter(lambda book : (book.authorName == authorName and book.id == bookId), books))

from dao.daoInterface.BookInterface import BookInterface

class BookStorage(BookInterface):

    books = [
            Book(id = "Book-1", name="Life", pageCount=10, authorName="Udit"),
            Book(id = "Book-2", name="Sea", pageCount=10, authorName="Sandeep"),
            Book(id = "Book-3", name="Land", pageCount=10, authorName="Kanishk"),
            Book(id = "Book-4", name="Life-2", pageCount=10, authorName="Udit")
        ]

    def getById(self, id: str) -> Book:
        listBook = list(filter(lambda book: book.id == id, self.books))
        return listBook[0]

    def getBookByAuthorAndId(self, authorName: str, bookId: str) -> List[Book]:
        return list(filter(lambda book : (book.authorName == authorName and (bookId == None  or book.id == bookId)), self.books))