import strawberry
from entities.Book import Book
from dao.daoInterface.BookInterface import BookInterface
import setting

bookDao: BookInterface = setting.bookDao
class BookQuery:

    @strawberry.field
    def book(self, id: str) -> Book:
        return bookDao.getById(id)