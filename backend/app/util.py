from typing import Any
from datetime import datetime

def row_to_json(row, props):
    d = {}
    idx = 0
    print("row to json")
    for prop in props:
        val = row[idx]
        print(str(val) + " " + str(type(val)))
        if type(val) is datetime:
            val = val.isoformat()
        d[prop] = val
        idx += 1
    return d

class DbModel:
    def __init__(self):
        pass

def tuple_to_db_object(tup, schema):
    model = DbModel()
    for i in range(len(schema)):
        setattr(model, schema[i], tup[i])
    print(tup, schema)
    return model

def rows_to_json(rows, props):
    print("rows:", rows)
    print("props:", props)
    if type(rows) == tuple:
        return row_to_json(rows, props)
    elif type(rows) == list:
        d_list = []
        d = {"data" : d_list}
        for row in rows:
            d1 = row_to_json(row, props)
            d_list.append(d1)
        return d
    return None
