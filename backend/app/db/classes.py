from pydantic import BaseModel

class Book(BaseModel):
    id: int = 0
    categoryId: int
    name: str
    description: str = None
    # type - paper / electronic
    type: str
    lang: str
    author: str
    pages: int
    publisher: str
    year: int
    coverFilePath: str = None

class BookCategory(BaseModel):
    id: int = 0
    name: str
