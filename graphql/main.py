import uvicorn
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry

from entities.Author import Author
from queries.UserQuery import UserQuery
from queries.BookQuery import BookQuery
from queries.CommentQuery import CommentQuery


@strawberry.type
class Query(UserQuery, BookQuery, CommentQuery):
    pass

schema  = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)