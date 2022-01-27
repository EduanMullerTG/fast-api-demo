from fastapi import FastAPI
from .schema import graphql_app


def create_app():
    app = FastAPI()

    app.include_router(graphql_app, prefix="/graphql")

    return app
