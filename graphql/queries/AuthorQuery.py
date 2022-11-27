import strawberry
from entities.Author import Author
from dao.daoInterface.AuthorInterface import AuthorInterface
import setting

authorDao: AuthorInterface = setting.authorDao

@strawberry.type
class AuthorQuery:

    @strawberry.field
    def author(self, name: str) -> Author:
        return authorDao.findAuthorByName(name)