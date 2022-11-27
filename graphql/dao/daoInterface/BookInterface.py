# It is an interface class for the Book dao

class BookInterface:
    def getById(self, id):
        pass

    def getBookByAuthor(self, authorName):
        pass

    def getBookByAuthorAndId(self, authorName, bookId):
        pass
