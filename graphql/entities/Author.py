import strawberry
from typing import Union, List, TYPE_CHECKING

import setting


if TYPE_CHECKING:
    from entities.Book import Book
    

@strawberry.type
class Author:
    id: Union[str,None] = None
    name: str
    age: int

    @strawberry.field
    def book(self, id: Union[str,None] = None) -> List[strawberry.LazyType["Book", "entities.Book"]]:
        return setting.bookDao.getBookByAuthorAndId(self.name, id)

