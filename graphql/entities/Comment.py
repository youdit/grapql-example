import strawberry
from typing import Union, TYPE_CHECKING

import setting

bookDao = None

if TYPE_CHECKING:
    from entities.Book import Book


@strawberry.type
class Comment:
    id: Union[str, None] = None
    text: str
    bookId: str

    @strawberry.field
    def book(self) -> strawberry.LazyType["Book","entities.Book"]:
        return setting.bookDao.getById(self.bookId)
