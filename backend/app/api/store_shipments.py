from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from db.classes import StoreShipment
from typing import Annotated
from db import db
from api.api_service import ApiService
from db.table_schemas import *
from util import *

database = db.database
router = APIRouter()
svc = ApiService(db.store_shipments_table, store_shipment_schema)
table_class = StoreShipment
base_path = "/store_shipments/"

@router.get(base_path, response_model=table_class)
def read_item():
    return svc.get_all_template()

@router.get(base_path + "{item_id}" + "/shipped_items/", response_model=table_class)
def get_shipped_items(item_id: int):
    return svc.get_items_by_id_template(db.get_table_by_name("store_shipped_items"), "storeShipmentId", item_id)

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
