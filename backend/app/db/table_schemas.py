from db.classes import *
book_schema = [ 'id', 'categoryId', 'name', 'description', 'type', 'lang', 'author', 'pages', 'publisher', 'year', 'coverFilePath' ]
book_category_schema = [ 'id', 'name' ]

def get_schema_by_type(type):
    if type == Book:
        return book_schema
    elif type == BookCategory:
        return book_category_schema