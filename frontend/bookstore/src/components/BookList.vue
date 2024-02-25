<template>
  <div class="book-list">
    <div>Book store network</div>
    <div class="book-item" :key="book.id" v-for="book in books.data">
      <img height="50" v-if="book.imageUrl != null" :src="book.imageUrl" alt="Fetched Image" />
      <p>Title: {{ book.name }}</p>
      <p>Author: {{ book.author }}</p>
      <p>Description: {{ book.description }}</p>
      <p>Category: {{ book.category != null ? book.category.name : "?" }}</p>
      <p>PUblisher: {{ book.publisher }}</p>
      <p>Year: {{ book.year }}</p>
      <p>Pages: {{ book.pages }}</p>
      <p>Type: {{ book.type }}</p>
      <p>Language: {{ book.lang }}</p>
      <p>Item ID: {{ book.id }}</p>
      <button @click="deleteBook($event, book.id)">Delete</button>
      <router-link :to="{ path: '/books/edit', query: { bookId: book.id } }">Edit book</router-link>
    </div>
  </div>
  <div>
    <div>
      <router-link to="/books/create">Add book</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [],
      imageUrls: {}
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    async deleteBook(event, bookId) {
      await window.axios.delete("/api/books/" + bookId)
      this.fetchData()
    },
    async fetchData() {
      console.log("before fetch all")
      let response = await fetch("http://localhost/api/books/")
      let data = await response.json()
      this.books = data
      await this.fetchCategories()
      await this.fetchImages()
    },
    async fetchCategories() {
      for (let book of this.books.data) {
        let response = await fetch("http://localhost/api/book_categories/" + book.categoryId)
        let data = await response.json()
        book.category = data
      }
    },
    async fetchImages() {
      for (let book of this.books.data) {
        this.fetchOneImage(book)
      }
    },
    async fetchOneImage(book) {
      let bookId = book.id
      try {
        const response = await fetch('/api/books/' + bookId + '/cover/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const blob = await response.blob();
        let url = URL.createObjectURL(blob);
        this.imageUrls[bookId] = url;
        book.imageUrl = url;
      } catch (error) {
        console.error('Error fetching image:', error);
      }
    },
    submitFile() {
      let formData = new FormData();
      formData.append('file_bytes', this.file)
      formData.append('key1', "value 1")
      formData.append('key2', "value NEW")
      window.axios.post("/api/files/", formData)
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