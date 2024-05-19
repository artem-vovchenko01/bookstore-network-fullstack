from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from typing import Annotated
from db import db
from api.api_service import ApiService
from db.table_schemas import *
from util import *

database = db.database
router = APIRouter()
base_path = "/admin/"

@router.get(base_path + "db_backup")
def backup_db():
    database.backup("db_backup" + ".pkl")
    return ApiService.get_sample()

@router.get(base_path + "db_restore")
def backup_db():
    database.restore("db_backup" + ".pkl")
    return ApiService.get_sample()

@router.get(base_path + "db_drop")
def backup_db():
    database.clear_db()
    return ApiService.get_sample()
