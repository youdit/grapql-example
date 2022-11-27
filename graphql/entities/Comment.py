import strawberry
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Book import Book

@strawberry.type
class Comment:
    id: Union[str, None] = None
    text: str
    bookId: str

    @strawberry.field
    def book(self) -> strawberry.LazyType["Book","entities.Book"]:
        from dao.BookStorage import getById
        return getById(self.bookId)
