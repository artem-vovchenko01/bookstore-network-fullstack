<template>
  <div class="book-category-list">
    <div>Book store network</div>
    <div class="book-category-item" :key="bookCategory.id" v-for="bookCategory in bookCategories.data">
      <p>Name: {{ bookCategory.name }}</p>
      <button @click="deleteBookCategory($event, bookCategory.id)">Delete</button>
      <button>
        <router-link class="router-link" :to="{ path: '/book_categories/edit', query: {bookCategoryId: bookCategory.id} }">Edit book category</router-link>
      </button>
    </div>
  </div>
  <div>
    <div>
      <button>
        <router-link to="/book_categories/create">Add book category</router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookCategories: []
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async deleteBookCategory(event, bookCategoryId) {
        await window.axios.delete("/api/book_categories/" + bookCategoryId)
        this.fetchData()
    },
    async fetchData() {
      let response = await fetch("http://localhost/api/book_categories/")
      let data = await response.json()
      this.bookCategories = data
    }
  }
}
</script>

<style scoped>
</style>