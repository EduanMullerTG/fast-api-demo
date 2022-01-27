import json
import strawberry

from typing import List
from pathlib import Path
from strawberry.fastapi import GraphQLRouter

from .types import Fruit

base_path = Path(__file__).parent


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    def get_fruit():
        with open((base_path / "data_files/fruit.json").resolve()) as file:
            data = json.load(file)

            result = []
            for fruit in data:
                result.append(Fruit(id=fruit["id"], name=fruit["name"]))

            return result

    fruit: List[Fruit] = strawberry.field(resolver=get_fruit)


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
