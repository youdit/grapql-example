import strawberry
from typing import Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Book import Book
    

@strawberry.type
class Author:
    id: Union[str,None] = None
    name: str
    age: int

    @strawberry.field
    def book(self) -> List[strawberry.LazyType["Book", "entities.Book"]]:
        from dao.BookStorage import getBookByAuthor
        return getBookByAuthor(self.name)

    @strawberry.field
    def book(self, id: str) -> List[strawberry.LazyType["Book", "entities.Book"]]:
        from dao.BookStorage import getBookByAuthorAndId
        return getBookByAuthorAndId(self.name, id)
