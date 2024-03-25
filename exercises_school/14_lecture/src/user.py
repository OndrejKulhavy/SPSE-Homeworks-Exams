from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    favorite_number: int
    favorite_color: str


