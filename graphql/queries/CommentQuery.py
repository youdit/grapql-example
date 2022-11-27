import strawberry
from entities.Comment import Comment
from dao.daoInterface.CommentInterface import CommentInterface
import setting

commentDao : CommentInterface = setting.commentDao
@strawberry.type
class CommentQuery:

    @strawberry.field
    def comment(self, id: str) -> Comment:
        return commentDao.getCommentById(id)
