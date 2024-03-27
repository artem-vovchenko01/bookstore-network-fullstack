import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';

import App from './App.vue';
import HeaderBar from './components/HeaderBar.vue';
import BookList from './components/BookList.vue';
import EditBook from './components/books/EditBook.vue';
import BookCategoryList from './components/book_categories/BookCategoryList.vue';
import EditBookCategory from './components/book_categories/EditBookCategory.vue';
import StoreList from './components/stores/StoreList.vue';
import EditStore from './components/stores/EditStore.vue';
import WarehouseList from './components/warehouses/WarehouseList.vue';
import EditWarehouse from './components/warehouses/EditWarehouse.vue';
import WarehouseShipmentList from './components/warehouse_shipments/WarehouseShipmentList.vue';
import EditWarehouseShipment from './components/warehouse_shipments/EditWarehouseShipment.vue';
import StoreShipmentList from './components/store_shipments/StoreShipmentList.vue';
import EditStoreShipment from './components/store_shipments/EditStoreShipment.vue';
import StoreStoredItemList from './components/store_stored_items/StoreStoredItemList.vue';
import WarehouseStoredItemList from './components/warehouse_stored_items/WarehouseStoredItemList.vue';
import UserList from './components/users/UserList.vue';
import EditUser from './components/users/EditUser.vue';
import PermissionList from './components/permissions/PermissionList.vue';
window.axios = require('axios');

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/books", component: BookList }, 
        { path: "/books/create", component: EditBook },
        { path: "/books/edit", component: EditBook },

        { path: "/book_categories", component: BookCategoryList }, 
        { path: "/book_categories/create", component: EditBookCategory },
        { path: "/book_categories/edit", component: EditBookCategory },

        { path: "/stores", component: StoreList }, 
        { path: "/stores/create", component: EditStore },
        { path: "/stores/edit", component: EditStore },

        { path: "/warehouses", component: WarehouseList }, 
        { path: "/warehouses/create", component: EditWarehouse },
        { path: "/warehouses/edit", component: EditWarehouse },

        { path: "/warehouses", component: WarehouseList }, 
        { path: "/warehouses/create", component: EditWarehouse },
        { path: "/warehouses/edit", component: EditWarehouse },

        { path: "/warehouse_shipments", component: WarehouseShipmentList }, 
        { path: "/warehouse_shipments/create", component: EditWarehouseShipment },
        { path: "/warehouse_shipments/edit", component: EditWarehouseShipment },

        { path: "/store_shipments", component: StoreShipmentList }, 
        { path: "/store_shipments/create", component: EditStoreShipment },
        { path: "/store_shipments/edit", component: EditStoreShipment },

        { path: "/store_stored_items", component: StoreStoredItemList },

        { path: "/warehouse_stored_items", component: WarehouseStoredItemList },

        { path: "/users", component: UserList },
        { path: "/users/create", component: EditUser },
        { path: "/users/edit", component: EditUser },

        { path: "/permissions", component: PermissionList },
    ]
});

const app = createApp(App);

app.component('header-bar', HeaderBar);

app.component('book-list', BookList);
app.component('edit-book', EditBook);

app.component('book-category-list', BookCategoryList);
app.component('edit-book-category', EditBookCategory);

app.component('store-list', StoreList);
app.component('edit-store', EditStore);

app.component('warehouse-list', WarehouseList);
app.component('edit-warehouse', EditWarehouse);

app.component('warehouse-shipment-list', WarehouseShipmentList);
app.component('edit-warehouse-shipment', EditWarehouseShipment);

app.component('store-shipment-list', StoreShipmentList);
app.component('edit-store-shipment', EditStoreShipment);

app.component('store-stored-item-list', StoreStoredItemList);

app.component('warehouse-stored-item-list', WarehouseStoredItemList);

app.use(router);

app.mount('#app');
