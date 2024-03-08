<template>
    <div>
        <img height="50" v-if="book.imageUrl != null" :src="book.imageUrl" alt="Fetched Image" />
        <br />

        <label for="input-file" class="custom-file-upload">Cover image</label>
        <input id="input-file" class="file-upload-class" type="file" @change="handleFileUpload($event)" />
        <br />

        <label for="name">Name</label>
        <input id="name" v-model.trim="book.name" type="text" />
        <br />

        <label for="description">Description</label>
        <input @input="validate($event)" id="description" v-model.number="book.description" type="text" />
        <br />

        <label for="category">Category</label>
        <select v-model="book.category" id="category">
            <option v-for="item in bookCategories" :key="item.id" :value="item">
                {{ item.name }}
            </option>
        </select>
        <br />

        <label for="book.type">Type</label>
        <input @input="validate($event)" id="type" v-model.number="book.type" type="text" />
        <br />

        <label for="book.lang">Language</label>
        <input @input="validate($event)" id="language" v-model.number="book.lang" type="text" />
        <br />

        <label for="book.publisher">Publisher</label>
        <input @input="validate($event)" id="publisher" v-model.number="book.publisher" type="text" />
        <br />

        <label for="book.pages">Number of pages</label>
        <input @input="validate($event)" id="pages" v-model.number="book.pages" type="number" />
        <br />

        <label for="book.year">Year</label>
        <input @input="validate($event)" id="year" v-model.number="book.year" type="number" />
        <br />

        <label for="book.author">Author</label>
        <input @input="validate($event)" id="author" v-model.number="book.author" type="text" />
        <br />

        <button @click="submitBook">
            {{ editBook ? "Save changes" : "Create" }}                
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            book: {},
            bookCategories: [],
            imageUrls: {},
            editBook: false
        }
    },
    async mounted() {
        await this.fetchBookCategories()
        if (this.$route.path === "/books/edit") {
            this.editBook = true
            this.book.id = this.$route.query.bookId
            let response = await fetch("http://localhost/api/books/" + this.book.id)
            let book = await response.json()
            this.book = book
            await this.fetchInitialCategory(book)
            this.fetchImage(book)
        }
    },
    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async fetchBookCategories() {
            let response = await fetch("http://localhost/api/book_categories/")
            let data = await response.json()
            this.bookCategories = data.data
        },
        async fetchInitialCategory(book) {
            let response = await fetch("http://localhost/api/book_categories/" + book.categoryId)
            let category = await response.json()
            book.category = category
        },
        async fetchImage(book) {
            let bookId = book.id
            try {
                let response = await fetch('/api/books/' + bookId + '/cover/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                let blob = await response.blob();
                let url = URL.createObjectURL(blob);
                this.imageUrls[bookId] = url;
                this.book.imageUrl = url;
                this.book.image = blob;
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        },
        async submitBook() {
            let formData = new FormData();
            formData.append('cover', this.book.image)
            let bookData = {
                "name": this.book.name,
                "description": this.book.description,
                "categoryId": this.book.category.id,
                "author": this.book.author,
                "pages": this.book.pages,
                "publisher": this.book.publisher,
                "type": this.book.type,
                "lang": this.book.lang,
                "year": this.book.year
            }
            let responseData = null
            if (this.editBook) {
                bookData.id = this.book.id
                responseData = await window.axios.put("/api/books/" + this.book.id, bookData, {
                    validateStatus: status => status >= 200
                });
            } else {
                responseData = await window.axios.post("/api/books/", bookData, {
                    validateStatus: status => status >= 200
                });
            }
            let bookId = 0;
            if (this.editBook) {
                bookId = this.book.id
            } else {
                bookId = responseData.data.id;
            }
            await window.axios.post("/api/books/" + bookId + "/cover/", formData)
            this.$router.push("/books/")
        },
        handleFileUpload(event) {
            this.book.image = event.target.files[0]
            let url = URL.createObjectURL(this.book.image);
            this.imageUrls[this.book.id] = url;
            this.book.imageUrl = url;
        }
    }
}
</script>

<style scoped>
book_item {
    width: 100em;
    border-width: 1px;
    border-style: solid;
    border-color: gray;
}
</style>