import mariadb
import sys
from pydantic import BaseModel
from typing import Optional
from .classes import *
from util import *
from db.table_schemas import *

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
        return str_rep

    def create_table(self, name, obj_class):
        cursor = self.conn.cursor()
        custom_props = self.get_cusom_props(obj_class)
        table = DbTable(name, obj_class)
        cols = obj_class.__annotations__
        command = "CREATE TABLE IF NOT EXISTS " + name + " ("
        for name, cls in cols.items():
            command += " " + name + " " + self.get_type_sql_str(cls)
            if name == 'id':
                command += " AUTO_INCREMENT PRIMARY KEY"
            command += ","
        command = command[:-1] 
        command += ");"
        print("Creating a table with command:")
        print(command)
        cursor.execute(command)
        print("Command ran")
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
        query = query[:-2]
        query += ");"
        # self.cursor.execute(query, (item.name, item.description))
        print("Executing query: ")
        print(query)
        cursor.execute(query)
        print("Ran execution")
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
        if item is None:
            self.insert(table, obj, at_id=obj.id)
            return obj
        cursor = self.conn.cursor()
        query = "UPDATE " + table.name + " SET "
        annotations = table.obj_class.__annotations__
        for name, cls in annotations.items():
            val = getattr(obj, name)
            if val is None:
                query += name + " = NULL, "
            else:
                if cls == int:
                    query += name + " = " + str(val) + ", "
                elif cls == str:
                    query += name + " = " +  "'" + val + "'" + ", "
        query = query[:-2]
        query += " WHERE id = " + str(obj.id) + ";"
        # self.cursor.execute(query, (item.name, item.description))
        print("Executing put query: ")
        print(query)
        cursor.execute(query)
        print("Ran execution")
        self.conn.commit()
        cursor.close()
        return obj

    def remove(self, table, id):
        cursor = self.conn.cursor()
        query = "DELETE FROM " + table.name + " WHERE id = " + str(id) + ";"
        print("Removing item with query")
        print(query)
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def get(self, table, id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM " + table.name + " WHERE id = " + str(id)  + ";"
        print("Ruuning GET query")
        print(query)
        cursor.execute(query)
        item = cursor.fetchone()
        print("Received item")
        print(item)
        cursor.close()
        return item

    def get_all(self, table):
        cursor = self.conn.cursor()
        query = "SELECT * FROM " + table.name + ";"
        print("Ruuning GET query (whole table)")
        print(query)
        cursor.execute(query)
        items = cursor.fetchall()
        print("Received items")
        print(items)
        cursor.close()
        return items

database = None
if database is None:
    database = Db()
    database.connect()
    books_table = database.create_table("books", Book)
    book_categories_table = database.create_table("book_categories", BookCategory)
