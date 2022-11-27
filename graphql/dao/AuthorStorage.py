from entities.Author import Author

users = [Author(name = "Udit", age = 24), Author(name = "Sandeep", age = 23), Author(name = "Kanishk", age = 22)]

def findAuthorByName(name: str) -> Author:
    userlist = list(filter(lambda user : user.name == name, users))
    return userlist[0]