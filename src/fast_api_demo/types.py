import strawberry


@strawberry.type
class Fruit:
    id: int
    name: str = strawberry.field(description="The common name of the fruit in English")
