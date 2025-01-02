from pydantic import BaseModel, ConfigDict


class Book(BaseModel):
    title: str


class BookPublic(BaseModel):
    book_id: int
    title: str
    model_config = ConfigDict(from_attributes=True)
