from pydantic import BaseModel
from datetime import datetime, date, time

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

class Warehouse(BaseModel):
    id: int = 0
    country: str
    city: str
    address: str
    capacity: int
    utilization: int

class WarehouseShipment(BaseModel):
    id: int = 0
    created: datetime
    arrived: datetime
    processed: datetime
    warehouseId: int
    supplier: str

class WarehouseShippedItem(BaseModel):
    id: int = 0
    bookId: int
    quantity: int
    warehouseShipmentId: int
    
class WarehouseStoredItem(BaseModel):
    id: int = 0
    bookId: int
    quantity: int
    warehouseId: int

class Store(BaseModel):
    id: int = 0
    country: str
    city: str
    address: str
    capacity: int
    utilization: int = 0
    worksFrom: int
    worksUntil: int
    workingDays: int

class StoreShipment(BaseModel):
    id: int = 0
    created: datetime
    departed: datetime
    arrived: datetime
    processed: datetime
    storeId: int
    warehouseId: str

class StoreShippedItem(BaseModel):
    id: int = 0
    bookId: int
    quantity: int
    storeShipmentId: int

class StoreStoredItem(BaseModel):
    id: int = 0
    bookId: int
    quantity: int
    storeId: int

class User(BaseModel):
    id: int = 0
    username: str
    password: str
    name: str = None
    surname: str = None
    age: int = None
    email: str = None
    phone: str = None
    country: str = None
    city: str = None

class Permission(BaseModel):
    id: int = 0
    resourceType: int
    correspondingItemId: int
    allowedAction: int
    userId: int
