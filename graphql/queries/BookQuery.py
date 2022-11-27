import strawberry
from entities.Book import Book
from dao.BookStorage import getById

@strawberry.type
class BookQuery:
    @strawberry.field
    def book(self, id: str) -> Book:
        return getById(id)