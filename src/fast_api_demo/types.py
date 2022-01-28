import base64
import strawberry

from typing import List, NewType


@strawberry.type
class Fruit:
    id: int
    name: str = strawberry.field(description="The common name of the fruit in English")


@strawberry.type
class Author:
    id: int
    name: str
    books: List["Book"]


@strawberry.type
class Book:
    id: int
    title: str
    author: Author


Base64 = strawberry.scalar(
    NewType("Base64", bytes),
    serialize=lambda v: base64.b64encode(v).decode("utf-8"),
    parse_value=lambda v: base64.b64decode(v.encode("utf-8")),
)
