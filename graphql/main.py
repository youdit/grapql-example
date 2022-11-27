import uvicorn
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry

import setting
from dao.daoInMemImpl.AuthorStorage import AuthorStorage
from dao.daoInMemImpl.CommentStorage import CommentStorage
from dao.daoInMemImpl.BookStorage import BookStorage

setting.authorDao = AuthorStorage()
setting.bookDao = BookStorage()
setting.commentDao = CommentStorage()


import queries.AuthorQuery as AuthorQuery
import queries.BookQuery as BookQuery
import queries.CommentQuery as CommentQuery


@strawberry.type
class Query(AuthorQuery.AuthorQuery, BookQuery.BookQuery, CommentQuery.CommentQuery):
    pass

schema  = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)