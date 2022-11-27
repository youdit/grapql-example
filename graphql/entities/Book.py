import strawberry
from typing import Union, TYPE_CHECKING, List

import setting


commentDao  = None
authorDao  = None

if TYPE_CHECKING:
    from entities.Author import Author
    from entities.Comment import Comment

@strawberry.type
class Book:
    id: Union[str, None]
    name: str
    pageCount: int
    authorName: str

    @strawberry.field
    def author(self) -> strawberry.LazyType["Author", "entities.Author"]:
        return setting.authorDao.findAuthorByName(self.authorName)

    @strawberry.field
    def comment(self) -> List[strawberry.LazyType["Comment", "entities.Comment"]]:
        return setting.commentDao.getCommentFormBookId(self.id)

