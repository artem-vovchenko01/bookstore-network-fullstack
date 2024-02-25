from db.classes import *
book_schema = [ 'id', 'categoryId', 'name', 'description', 'type', 'lang', 'author', 'pages', 'publisher', 'year', 'coverFilePath' ]
book_category_schema = [ 'id', 'name' ]
warehouse_schema = [ 'id', 'country', 'city', 'address', 'capacity', 'utilization' ]
warehouse_shipment_schema = [ 'id', 'created', 'arrived', 'processed', 'warehouseId', 'supplier' ]
warehouse_shipped_item_schema = [ 'id', 'bookId', 'quantity', 'warehouseShipmentId' ]
warehouse_stored_item_schema = [ 'id', 'bookId', 'quantity', 'warehouseId' ]
store_schema = [ 'id', 'country', 'city', 'address', 'capacity', 'utilization', 'worksFrom', 'worksUntil', 'workingDays' ]
store_shipment_schema = [ 'id', 'created', 'departed', 'arrived', 'processed', 'storeId', 'warehouseId' ]
store_shipped_item_schema = [ 'id', 'bookId', 'quantity', 'storeShipmentId' ]
store_stored_item_schema = [ 'id', 'bookId', 'quantity', 'storeId' ]
user_schema = [ 'id', 'username', 'password', 'name', 'surname', 'age', 'email', 'phone', 'country', 'city' ]
permission_schema = [ 'id', 'resourceType', 'correspondingItemId', 'allowedAction', 'userId' ]

def get_schema_by_type(type):
    if type == Book:
        return book_schema
    elif type == BookCategory:
        return book_category_schema
    elif type == Warehouse:
        return warehouse_schema
    elif type == WarehouseShipment:
        return warehouse_shipment_schema
    elif type == WarehouseShippedItem:
        return warehouse_shipped_item_schema
    elif type == WarehouseStoredItem:
        return warehouse_stored_item_schema
    elif type == Store:
        return store_schema
    elif type == StoreShipment:
        return store_shipment_schema
    elif type == StoreShippedItem:
        return store_shipped_item_schema
    elif type == StoreShippedItem:
        return store_shipped_item_schema
    elif type == StoreStoredItem:
        return store_stored_item_schema
    elif type == User:
        return user_schema
    elif type == Permission:
        return permission_schema