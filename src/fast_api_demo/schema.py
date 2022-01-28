import json
import strawberry

from typing import List
from pathlib import Path

# from fastapi import Depends
# from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from .types import Fruit, Base64, Author, Book

# from .database import SessionLocal, engine, Base

# Base.metadata.create_all(bind=engine)

base_path = Path(__file__).parent


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    def get_all_fruit():
        with open((base_path / "data_files/fruit.json").resolve()) as file:
            data = json.load(file)

            result = []
            for fruit in data:
                result.append(Fruit(id=fruit["id"], name=fruit["name"]))

            return result

    @strawberry.field
    def fruit(self, id: int) -> Fruit:
        with open((base_path / "data_files/fruit.json").resolve()) as file:
            data = list(json.load(file))
            print(data)
            result = next(fruit for fruit in data if fruit["id"] == id)

            return Fruit(id=result["id"], name=result["name"])

    @strawberry.field
    def fruit_file() -> Base64:
        with open((base_path / "data_files/fruit.json").resolve(), "rb") as file:
            return Base64(file.read())

    # @strawberry.field
    # def authors(self, db: Session = Depends(get_db)) -> Author:
    #     return Author()

    all_fruit: List[Fruit] = strawberry.field(resolver=get_all_fruit)


@strawberry.type
class Mutation:
    @strawberry.field
    def add_fruit(self, name: str) -> Fruit:
        with open((base_path / "data_files/fruit.json").resolve(), "r+") as file:
            data = list(json.load(file))
            new_id = len(data)
            data.append({"id": new_id, "name": name})

            file.seek(0)
            file.write(json.dumps(data))

            return Fruit(id=new_id, name=name)


schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema, "", True)
