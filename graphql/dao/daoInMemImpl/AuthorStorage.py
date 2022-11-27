from entities.Author import Author

# users = [Author(name = "Udit", age = 24), Author(name = "Sandeep", age = 23), Author(name = "Kanishk", age = 22)]

# def findAuthorByName(name: str) -> Author:
#     userlist = list(filter(lambda user : user.name == name, users))
#     return userlist[0]

from dao.daoInterface.AuthorInterface import AuthorInterface

class AuthorStorage(AuthorInterface):
    users = [Author(name = "Udit", age = 24), Author(name = "Sandeep", age = 23), Author(name = "Kanishk", age = 22)]

    def findAuthorByName(self, name: str) -> Author:
        userlist = list(filter(lambda user : user.name == name, self.users))
        return userlist[0]