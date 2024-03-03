<template>
  <div class="store-stored-item-list">
    <div>Book store network</div>
    <div class="store-stored-item" :key="storeStoredItem.id" v-for="storeStoredItem in storeStoredItems.data">
      <p>Book title: {{ 'book' in storeStoredItem ? storeStoredItem.book.name : "loading ..." }}</p>
      <p>Available: {{ 'book' in storeStoredItem ? storeStoredItem.quantity : "loading ..." }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      storeStoredItems: [],
      frontendPath: "/store_stored_items/",
      backendPath: "/api/store_stored_items/",
      booksPath: "/api/books/"
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      let response = await fetch(this.backendPath)
      let data = await response.json()
      this.storeStoredItems = data
      console.log("data: ", data)
      await this.fetchBooks()
    },
    async fetchBooks() {
      for (let storeStoredItem of this.storeStoredItems.data) {
        let response = await fetch(this.booksPath + storeStoredItem.bookId)
        let data = await response.json()
        storeStoredItem.book = data
      }
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