<template>
  <div class="item-list">
    <div>Book store network</div>
    <div class="item" :key="item.id" v-for="item in items.data">
      <p>Item ID: {{ item.id }}</p>
      <p>Date created: {{ item.created }}</p>
      <p>Date arrived: {{ ('arrived' in item) ? item.arrived : "-" }}</p>
      <p>Date processed: {{ ('processed' in item) ? item.processed : "-" }}</p>
      <p v-if="('store' in item)">Store: {{ item.store.id + ", "  + item.store.country + ", " + item.store.city + ", " + item.store.address }}</p>
      <p>Supplier: {{ item.supplier }}</p>
      <button @click="deleteItem($event, item.id)">Delete</button>
      <router-link :to="{ path: this.frontendPath + '/edit', query: {storeShipmentId: item.id} }">Edit store shipment</router-link>
    </div>
  </div>
  <div>
    <div>
      <router-link :to="{ path: this.frontendPath + '/create'}">Add store shipment</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      frontendPath: "/store_shipments",
      backendPath: "/api/store_shipments"
    }
  },
  async mounted() {
    await this.fetchData()
    this.fetchStores()
  },
  methods: {
    async deleteItem(event, itemId) {
        console.log(itemId, event)
        await window.axios.delete(this.backendPath + "/" + itemId)
        await this.fetchData()
    },
    async fetchStores() {
      console.log("fetching stores")
      for (let obj of this.items.data) {
        console.log("req: ", "/api/stores/" + obj.storeId)
        let response = await fetch("/api/stores/" + obj.storeId)
        let data = await response.json()
        console.log("obj: ", obj)
        obj.store = data
      }
    },
    async fetchData() {
      console.log("fetching data")
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