<template>
  <div class="book-list">
    <div class="book-item" :key="book.id" v-for="book in books.data">
      <div class="book-cover">
        <img height="50" v-if="book.imageUrl != null" :src="book.imageUrl" alt="Fetched Image" />
      </div>
      <div class="book-info">
        <p class="book-name">Title: {{ book.name }}</p>
        <p>Author: {{ book.author }}</p>
        <p>Description: {{ book.description }}</p>
        <!-- <p>Category: {{ book.category != null ? book.category.name : "?" }}</p>
        <p>PUblisher: {{ book.publisher }}</p>
        <p>Year: {{ book.year }}</p>
        <p>Pages: {{ book.pages }}</p>
        <p>Type: {{ book.type }}</p>
        <p>Language: {{ book.lang }}</p>
        <p>Item ID: {{ book.id }}</p> -->
        <button @click="deleteBook($event, book.id)">Delete</button>
        <button>
          <router-link :to="{ path: '/books/edit', query: { bookId: book.id } }">Edit book</router-link>
        </button>
      </div>
    </div>
  </div>
  <div>
    <div>
      <button>
        <router-link to="/books/create">Add book</router-link>
      </button>
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

.book-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
}

.book-item {
  background-color: #F5F5DC; /* Or #F0F0F0 for a cooler tone */
    color: #333333;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.book-cover img {
    width: 100%;
    height: auto;
}

.book-info {
    padding: 10px;
    flex-grow: 1;
}

.book-name {
    font-size: 16px;
    font-weight: bold;
    margin: 0 0 10px 0;
}

.book-price {
    font-size: 14px;
    color: #007bff;
}

</style>