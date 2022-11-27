import strawberry
from entities.Comment import Comment
from dao.CommentStorage import getCommentById

@strawberry.type
class CommentQuery:
    @strawberry.field
    def comment(self, id: str) -> Comment:
        return getCommentById(id)
