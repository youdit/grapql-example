import strawberry
from typing import Union, TYPE_CHECKING, List


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
        from dao.AuthorStorage import findAuthorByName
        return findAuthorByName(self.authorName)

    @strawberry.field
    def comment(self) -> List[strawberry.LazyType["Comment", "entities.Comment"]]:
        from dao.CommentStorage import getCommentFormBookId
        return getCommentFormBookId(self.id)

