from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from db.classes import Book
from typing import Annotated
from db import db
from api.api_service import ApiService
from db.table_schemas import *
from util import *

database = db.database
router = APIRouter()
svc = ApiService(db.books_table, book_schema)
table_class = Book
base_path = "/books/"
picture_path = "/data/books/covers"

@router.post("/files/")
def upload_file_bytes(file_bytes: bytes = File(...), key1: str = Form(...), key2: str = Form(...)):
    print(type(file_bytes))
    print("key1: ", key1)
    print("key2: ", key2)
    with open("/file.jpg", 'wb') as file:
        file.write(file_bytes)
    return {'file_bytes': str(file_bytes)}

@router.get("/files/")
def get_file():
    file_path = "/file.jpg"
    try:
        return FileResponse(path=file_path, filename="desired_filename.jpg")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {e}")

@router.get(base_path, response_model=table_class)
def read_item():
    return svc.get_all_template()

@router.get(base_path + "{item_id}/cover/")
def get_picture(item_id: int):
    file_path = f"{picture_path}/{item_id}.jpg"
    try:
        return FileResponse(path=file_path, filename=f"{item_id}.jpg")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {e}")

@router.post(base_path + "{item_id}/cover/")
def upload_picture(item_id: int, cover: bytes = File(...)):
    print("item id: ", item_id)
    coverPath = "/data/books/covers/" + str(item_id) + ".jpg"
    with open(coverPath, 'wb') as file:
        file.write(cover)
    item = svc.raw_get_template(item_id)
    print("got raw item: ", item)
    print("item: ", item)
    item_temp = list(item)
    item_temp[10] = coverPath
    item = list(item_temp)
    print("item: ", item)
    svc.update_template(item_id, item)
    return {'file_bytes': str(cover)}

#@router.post(base_path, response_model=table_class)
@router.post(base_path, response_model=table_class)
def create_item(item: table_class):
    print("posted /books =============================================================")
    print("item: ", item)
    return svc.create_template(item)

@router.get(base_path + "{item_id}", response_model=table_class)
def read_item(item_id: int):
    return svc.get_template(item_id)

@router.put(base_path + "{item_id}", response_model=table_class)
def update_item(item_id: int, item: table_class):
    return svc.update_template(item_id, item)

@router.delete(base_path + "{item_id}", response_model=table_class)
def delete_item(item_id: int):
    return svc.delete_template(item_id)