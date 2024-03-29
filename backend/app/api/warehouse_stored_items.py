from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from db.classes import WarehouseStoredItem
from typing import Annotated
from db import db
from api.api_service import ApiService
from db.table_schemas import *
from util import *

database = db.database
router = APIRouter()
svc = ApiService(db.warehouse_stored_items_table, warehouse_stored_item_schema)
table_class = WarehouseStoredItem
base_path = "/warehouse_stored_items/"

@router.get(base_path, response_model=table_class)
def read_item():
    return svc.get_all_template()

@router.get(base_path + "by_warehouse/{warehouse_id}/by_book/{book_id}", response_model=table_class)
def get_by_book_and_warehouse(warehouse_id: int, book_id: int):
    return svc.filter_template(db.get_table_by_name("warehouse_stored_items"), ("bookId", book_id), ("warehouseId", warehouse_id))

@router.post(base_path, response_model=table_class)
def create_item(item: table_class):
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
