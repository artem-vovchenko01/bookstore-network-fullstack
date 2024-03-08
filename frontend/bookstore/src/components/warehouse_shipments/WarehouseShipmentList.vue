<template>
  <div class="item-list">
    <div>Book store network</div>
    <div class="item" :key="item.id" v-for="item in items.data">
      <p>Item ID: {{ item.id }}</p>
      <p>Date created: {{ item.created }}</p>
      <p>Date arrived: {{ ('arrived' in item) ? item.arrived : "-" }}</p>
      <p>Date processed: {{ ('processed' in item) ? item.processed : "-" }}</p>
      <p v-if="('warehouse' in item)">Warehouse: {{ item.warehouse.id + ", "  + item.warehouse.country + ", " + item.warehouse.city + ", " + item.warehouse.address }}</p>
      <p>Supplier: {{ item.supplier }}</p>
      <button @click="deleteItem($event, item.id)">Delete</button>
      <button>
        <router-link :to="{ path: this.frontendPath + '/edit', query: {warehouseShipmentId: item.id} }">Edit warehouse shipment</router-link>
      </button>
    </div>
  </div>
  <div>
    <div>
      <button>
        <router-link :to="{ path: this.frontendPath + '/create'}">Add warehouse shipment</router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      frontendPath: "/warehouse_shipments",
      backendPath: "/api/warehouse_shipments"
    }
  },
  async mounted() {
    await this.fetchData()
    this.fetchWarehouses()
  },
  methods: {
    async deleteItem(event, itemId) {
        console.log(itemId, event)
        await window.axios.delete(this.backendPath + "/" + itemId)
        await this.fetchData()
    },
    async fetchWarehouses() {
      console.log("fetching warehouses")
      for (let obj of this.items.data) {
        console.log("req: ", "/api/warehouses/" + obj.warehouseId)
        let response = await fetch("/api/warehouses/" + obj.warehouseId)
        let data = await response.json()
        console.log("obj: ", obj)
        obj.warehouse = data
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