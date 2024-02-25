from typing import Any

def row_to_json(row, props):
    d = {}
    id = 0
    for prop in props:
        d[prop] = row[id]
        id += 1
    return d

class DbModel:
    def __init__(self):
        pass

def tuple_to_db_object(tup, schema):
    model = DbModel()
    for i in range(len(schema)):
        setattr(model, schema[i], tup[i])
    return model

def rows_to_json(rows, props):
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
