from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse
from db import db
from util import *

class ApiService:
    def __init__(self, table, schema):
        self.table = table
        self.database = db.database
        self.schema = schema

    def get_all_template(self):
        items = self.database.get_all(self.table)
        print(items)
        if items is None:
            raise HTTPException(status_code=404, detail="Items were not found")
        return JSONResponse(content=rows_to_json(items, self.schema))

    def filter_template(self, table, *filters):
        items = self.database.filter(table, *filters)
        print(items)
        if items is None:
            raise HTTPException(status_code=404, detail="Items were not found")
        return JSONResponse(content=rows_to_json(items, table.schema))

    def create_template(self, item):
        item.id = self.database.insert(self.table, item)
        return JSONResponse(content={ "id" : item.id })

    def raw_get_template(self, item_id: int):
        item = self.database.get(self.table, item_id)
        print(f"get item by id {self.table}")
        return item

    def get_template(self, item_id: int):
        item = self.database.get(self.table, item_id)
        print(f"get item by id {self.table}")
        print(item)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JSONResponse(content = rows_to_json(item, self.schema))

    def update_template(self, item_id: int, item):
        item = self.database.put(self.table, item)
        return item

    def delete_template(self, item_id: int):
        self.database.remove(self.table, item_id)
        return JSONResponse(content={"id": item_id})