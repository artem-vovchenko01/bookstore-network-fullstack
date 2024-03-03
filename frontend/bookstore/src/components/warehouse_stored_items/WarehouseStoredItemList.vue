<template>
  <div class="warehouse-stored-item-list">
    <div>Book store network</div>
    <div class="warehouse-stored-item" :key="warehouseStoredItem.id" v-for="warehouseStoredItem in warehouseStoredItems.data">
      <p>Book title: {{ ('book' in warehouseStoredItem) ? warehouseStoredItem.book.name : "loading ..." }}</p>
      <p>Available: {{ ('book' in warehouseStoredItem) ? warehouseStoredItem.quantity : "loading ..." }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      warehouseStoredItems: [],
      frontendPath: "/warehouse_stored_items/",
      backendPath: "/api/warehouse_stored_items/",
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
      this.warehouseStoredItems = data
      console.log("data: ", data)
      await this.fetchBooks()
    },
    async fetchBooks() {
      for (let warehouseStoredItem of this.warehouseStoredItems.data) {
        let response = await fetch(this.booksPath + warehouseStoredItem.bookId)
        let data = await response.json()
        warehouseStoredItem.book = data
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