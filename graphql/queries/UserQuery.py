import strawberry
from entities.Author import Author
from dao.AuthorStorage import findAuthorByName


@strawberry.type
class UserQuery:
    @strawberry.field
    def user(self, name: str) -> Author:
        return findAuthorByName(name)