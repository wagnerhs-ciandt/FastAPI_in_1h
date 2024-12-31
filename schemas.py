from uuid import uuid4

from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str


class BookPublic(BaseModel):
    book_id: str = Field(default_factory=lambda: uuid4().hex)
    title: str
