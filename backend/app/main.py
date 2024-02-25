from fastapi import FastAPI
from db import db
from api import books
from api import book_categories

app = FastAPI()

app.include_router(books.router)
app.include_router(book_categories.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #uvicorn.run(app, host="0.0.0.0", port=8000, log_level="trace")
