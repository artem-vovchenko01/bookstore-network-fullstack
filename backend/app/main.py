from fastapi import FastAPI
from db import db
from api import books
from api import book_categories
from api import warehouses
from api import warehouse_shipped_items
from api import warehouse_shipments
from api import warehouse_stored_items
from api import stores
from api import store_shipped_items
from api import store_shipments
from api import store_stored_items
from api import users
from api import permissions

app = FastAPI()

app.include_router(books.router)
app.include_router(book_categories.router)
app.include_router(warehouses.router)
app.include_router(warehouse_shipped_items.router)
app.include_router(warehouse_shipments.router)
app.include_router(warehouse_stored_items.router)
app.include_router(stores.router)
app.include_router(store_shipped_items.router)
app.include_router(store_shipments.router)
app.include_router(store_stored_items.router)
app.include_router(users.router)
app.include_router(permissions.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #uvicorn.run(app, host="0.0.0.0", port=8000, log_level="trace")
