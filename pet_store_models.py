from pydantic import BaseModel 
from typing import Literal

class Category (BaseModel):
    id: int
    name: str

class Pet (BaseModel):
    id: int | None = None
    category: Category | None = None
    name: str | None = None
    photoUrls: list[str]
    tags: list[Category]
    status: Literal["available", "pending", "sold"] | None = None

class DeletedPet (BaseModel):
    code: Literal[200]
    type: Literal["unknown"]
    message: str

class PetNotFoundError (BaseModel):
    code: Literal[1]
    type: Literal["error"]
    message: Literal["Pet not found"]

