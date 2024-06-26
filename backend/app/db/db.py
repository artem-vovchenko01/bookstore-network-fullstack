import mariadb
import sys
from pydantic import BaseModel
from typing import Optional
from .classes import *
from util import *
from db.table_schemas import *
from datetime import datetime, date, time
import pickle

class DummyModel(BaseModel):
    id: int = 0

class DbColumn:
    def __init__(self, name, type, nullable, props=None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.props = props

class DbTable:
    def __init__(self, name, obj_class):
        self.name = name
        self.obj_class = obj_class
        self.schema = get_schema_by_type(obj_class)

class Db:
    def __init__(self):
        self.tables = []

    def connect(self):
        try:
            conn = mariadb.connect(
                user="bookstore",
                password="bookstorepasswd",
                host="db",
                port=3306,
                database="bookstore"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        self.conn = conn

    def get_cursor(self):
        return self.conn.cursor()

    def get_cusom_props(self, obj_class):
        default_props = dir(DummyModel)
        found_props = set(dir(obj_class))
        custom_props = found_props.difference(set(default_props))
        return custom_props

    def get_type_sql_str(self, cls):
        str_rep = ""
        if cls == int:
            str_rep += "INT"
        elif cls == str:
            str_rep += "VARCHAR (255)"
        elif cls == Optional[int]:
            print("type we check is optional int")
            str_rep += "INT"
        elif cls == Optional[str]:
            print("type we check is optional str")
            str_rep += "VARCHAR (255)"
        elif cls == datetime:
            str_rep += "DATETIME"
        elif cls == Optional[datetime]:
            str_rep += "DATETIME"
        return str_rep

    def create_table(self, name, obj_class):
        cursor = self.conn.cursor()
        custom_props = self.get_cusom_props(obj_class)
        table = DbTable(name, obj_class)
        cols = obj_class.__annotations__
        command = "CREATE TABLE IF NOT EXISTS " + name + " ("
        table_name = name
        for name, cls in cols.items():
            command += " " + name + " " + self.get_type_sql_str(cls)
            if name == 'id':
                command += " AUTO_INCREMENT PRIMARY KEY"
            command += ","
        command = command[:-1] 
        command += ");"
        print(f"Creating table {table_name}")
        print(command)
        cursor.execute(command)
        self.tables.append(table)
        return table
 
    def insert(self, table, obj, at_id=None):
        cursor = self.conn.cursor()
        query = "INSERT INTO " + table.name + " ("
        annotations = table.obj_class.__annotations__
        for name, cls in annotations.items():
            if (name is not "id") or (at_id is not None):
                query += name + ", "
        query = query[:-2]
        query += ") VALUES ("
        for name, cls in annotations.items():
            val = getattr(obj, name)
            if (name is not "id") or (at_id is not None):
                if val is None:
                    query += "NULL, "
                else:
                    if cls == int:
                        query += str(val) + ", "
                    elif cls == str:
                        query += "'" + val + "', "
                    elif cls == datetime:
                        query += "'" + val.strftime('%Y-%m-%d %H:%M:%S') + "', "
        query = query[:-2]
        query += ");"
        print(f"Inserting {obj} into {table.name}")
        print(query)
        cursor.execute(query)
        self.conn.commit()
        item_id = cursor.lastrowid
        cursor.close()
        print("Last row id: ", item_id)
        return item_id

    def put(self, table, obj):
        try:
            __test_val = obj.id
        except:
            obj = tuple_to_db_object(obj, get_schema_by_type(table.obj_class))
        item = self.get(table, obj.id)
        print("===========================================")
        print(obj)
        print("===========================================")
        if item is None:
            self.insert(table, obj, at_id=obj.id)
            return obj
        cursor = self.conn.cursor()
        query = "UPDATE " + table.name + " SET "
        annotations = table.obj_class.__annotations__
        for name, cls in annotations.items():
            print(name, cls)
            val = getattr(obj, name)
            if val is None:
                query += name + " = NULL, "
            else:
                if cls == int:
                    query += name + " = " + str(val) + ", "
                elif cls == str:
                    query += name + " = " +  "'" + val + "'" + ", "
                elif cls == datetime:
                    query += name + " = " +  "'" + val.strftime('%Y-%m-%d %H:%M:%S') + "'" + ", "
        query = query[:-2]
        query += " WHERE id = " + str(obj.id) + ";"
        print(f"Put {obj} into {table.name}")
        print(query)
        cursor.execute(query)
        print("Ran execution")
        self.conn.commit()
        cursor.close()
        return obj

    def remove(self, table, id):
        cursor = self.conn.cursor()
        query = "DELETE FROM " + table.name + " WHERE id = " + str(id) + ";"
        print(f"Remove object {id} from {table.name}")
        print(query)
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def remove_all(self, table):
        cursor = self.conn.cursor()
        query = "DELETE FROM " + table.name + ";"
        print(f"Removed all objects from {table.name}")
        print(query)
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def clear_db(self):
        for table in self.tables:
            self.remove_all(table)

    def get(self, table, id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM " + table.name + " WHERE id = " + str(id)  + ";"
        print(f"Get object {id} from {table.name}")
        print(query)
        cursor.execute(query)
        item = cursor.fetchone()
        print("Got item")
        print(item)
        cursor.close()
        return item

    def get_all(self, table):
        cursor = self.conn.cursor()
        query = "SELECT * FROM " + table.name + ";"
        print(f"Get all from {table.name}")
        print(query)
        cursor.execute(query)
        items = cursor.fetchall()
        print("Got items")
        print(items)
        cursor.close()
        return items

    def backup(self, filename):
        backup_schema_dict = {}
        backup_data_dict = {}
        for table in self.tables:
            backup_schema_dict[table.name] = table
            backup_data_dict[table.name] = self.get_all(table)
        print("Starting backup process ...")
        print("Backup schema dict")
        print(backup_schema_dict)
        print("Backup data dict")
        print(backup_data_dict)
        with open(filename, "wb") as f:
            pickle.dump([backup_schema_dict, backup_data_dict], f)
    
    def restore(self, filename):
        backup_schema_dict = {}
        backup_data_dict = {}
        print("Starting restore process ...")
        with open(filename, "rb") as f:
            loaded = pickle.load(f)
            print("Loaded: ")
            print(loaded)
            backup_schema_dict, backup_data_dict = loaded
            print("Schema dict")
            print(backup_schema_dict)
            print("Data dict")
            print(backup_data_dict)
        self.clear_db()
        self.tables = [] 
        print("Tables are emptied")
        for table_name in backup_schema_dict.keys():
            table = backup_schema_dict[table_name]
            data = backup_data_dict[table_name]
            print(f"Appending table {table.name}")
            self.tables.append(table)
            for row in data:
                self.put(table, row)

    def get_items_by_id(self, child_table, col_name, id):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {child_table.name} WHERE {col_name} = {id};"
        print(f"Get items from {child_table.name} by {col_name} {id}")
        print(query)
        cursor.execute(query)
        items = cursor.fetchall()
        print("Got items")
        print(items)
        cursor.close()
        return items
    
    def filter(self, table, *filters):
        print("table: ", table)
        print("filters: ", filters)
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table.name} WHERE " 
        for filter in filters:
            col = filter[0]
            val = filter[1]
            query += f" {col} = {val} AND"
        query = query[:-4] + ";"
        print(f"Get items from {table.name} with filtering")
        print(f"filters: {filters}")
        print(query)
        print("before exec")
        cursor.execute(query)
        print("after exec")
        items = cursor.fetchall()
        print("after fetch")
        print("Got items")
        print(items)
        cursor.close()
        return items

def get_table_by_name(name):
    return list(filter(lambda t: t.name == name, database.tables))[0]

database = None
if database is None:
    database = Db()
    database.connect()
    books_table = database.create_table("books", Book)
    book_categories_table = database.create_table("book_categories", BookCategory)
    warehouses_table = database.create_table("warehouses", Warehouse)
    warehouse_shipments_table = database.create_table("warehouse_shipments", WarehouseShipment)
    warehouse_shipped_items_table = database.create_table("warehouse_shipped_items", WarehouseShippedItem)
    warehouse_stored_items_table = database.create_table("warehouse_stored_items", WarehouseStoredItem)
    stores_table = database.create_table("stores", Store)
    store_shipments_table = database.create_table("store_shipments", StoreShipment)
    store_shipped_items_table = database.create_table("store_shipped_items", StoreShippedItem)
    store_stored_items_table = database.create_table("store_stored_items", StoreStoredItem)
    users_table = database.create_table("users", User)
    permissions_table = database.create_table("permissions", Permission)