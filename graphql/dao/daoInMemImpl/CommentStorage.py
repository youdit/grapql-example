from entities.Comment import Comment
from typing import List

# comments = [
#     Comment(id="Comment-1", text="NiceBook", bookId="Book-1"),
#     Comment(id="Comment-2", text="Neet Book", bookId="Book-1"),
#     Comment(id="Comment-3", text="Nice Author", bookId="Book-1"),
#     Comment(id="Comment-4", text="full of ads", bookId="Book-2"),
#     Comment(id="Comment-5", text="Tought English", bookId="Book-2"),
#     Comment(id="Comment-6", text="Easy English", bookId="Book-3"),
#     Comment(id="Comment-7", text="Nice Story", bookId="Book-4"),
# ]

# def getCommentFormBookId(bookId: str) -> List[Comment]:
#     commentList = list(filter(lambda comment : comment.bookId == bookId, comments))
#     return commentList

# def getCommentById(id: str) -> Comment:
#     commentList = list(filter(lambda comment: comment.id == id, comments))
#     return commentList[0]

from dao.daoInterface.CommentInterface import CommentInterface

class CommentStorage(CommentInterface):

    comments = [
            Comment(id="Comment-1", text="NiceBook", bookId="Book-1"),
            Comment(id="Comment-2", text="Neet Book", bookId="Book-1"),
            Comment(id="Comment-3", text="Nice Author", bookId="Book-1"),
            Comment(id="Comment-4", text="full of ads", bookId="Book-2"),
            Comment(id="Comment-5", text="Tought English", bookId="Book-2"),
            Comment(id="Comment-6", text="Easy English", bookId="Book-3"),
            Comment(id="Comment-7", text="Nice Story", bookId="Book-4"),
        ]

    def getCommentFormBookId(self, bookId: str) -> List[Comment]:
        commentList = list(filter(lambda comment : comment.bookId == bookId, self.comments))
        return commentList

    def getCommentById(self, id: str) -> Comment:
        commentList = list(filter(lambda comment: comment.id == id, self.comments))
        return commentList[0]