<template>
  <div class="item-list">
    <div>Book store network</div>
    <div class="item" :key="item.id" v-for="item in items.data">
      <p>Name: {{ item.name }}</p>
      <p>Item ID: {{ item.id }}</p>
      <p>Country: {{ item.country }}</p>
      <p>City: {{ item.city }}</p>
      <p>Address: {{ item.address }}</p>
      <p>Capacity {{ item.capacity }}</p>
      <p>Utilization: {{ item.utilization }}</p>
      <button @click="deleteItem($event, item.id)">Delete</button>
      <router-link :to="{ path: this.frontendPath + '/edit', query: {warehouseId: item.id} }">Edit warehouse</router-link>
    </div>
  </div>
  <div>
    <div>
      <router-link :to="{ path: this.frontendPath + '/create'}">Add warehouse</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      frontendPath: "/warehouses",
      backendPath: "/api/warehouses"
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async deleteItem(event, itemId) {
        console.log(itemId, event)
        await window.axios.delete(this.backendPath + "/" + itemId)
        this.fetchData()
    },
    async fetchData() {
      let response = await fetch(this.backendPath + "/")
      let data = await response.json()
      this.items = data
    }
  }
}
</script>

<style scoped>
item {
  width: 100em;
  border-width: 1px;
  border-style: solid;
  border-color: gray;
}
</style>