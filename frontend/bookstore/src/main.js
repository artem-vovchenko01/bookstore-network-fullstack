import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';

import App from './App.vue';
import HeaderBar from './components/HeaderBar.vue';
import BookList from './components/BookList.vue';
import EditBook from './components/books/EditBook.vue';
import BookCategoryList from './components/book_categories/BookCategoryList.vue';
import EditBookCategory from './components/book_categories/EditBookCategory.vue';
window.axios = require('axios');

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/books", component: BookList }, 
        { path: "/books/create", component: EditBook },
        { path: "/books/edit", component: EditBook },

        { path: "/book_categories", component: BookCategoryList }, 
        { path: "/book_categories/create", component: EditBookCategory },
        { path: "/book_categories/edit", component: EditBookCategory }
    ]
});

const app = createApp(App);

app.component('header-bar', HeaderBar);

app.component('book-list', BookList);
app.component('edit-book', EditBook);

app.component('book-category-list', BookCategoryList);
app.component('edit-book-category', EditBookCategory);

app.use(router);

app.mount('#app');