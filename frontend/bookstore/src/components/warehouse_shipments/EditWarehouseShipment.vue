<template>
    <div>
        <button @click="restoreShipment()">Restore shipment</button>
        <button v-if="warehouseShipment.processed === null" @click="cancelShipment()">Cancel shipment</button>
        <button v-if="warehouseShipment.departed === null" @click="markShipmentAsDeparted()">Shipment departed from warehouse</button>
        <button v-if="warehouseShipment.arrived === null && warehouseShipment.departed !== null" @click="markShipmentAsArrived()">Shipment arrived to the store</button>
        <button v-if="warehouseShipment.processed === null && warehouseShipment.arrived !== null" @click="markShipmentAsProcessed()">Shipment was processed in the store</button>
        <label for="warehouse">Warehouse</label>
        <select v-model="warehouseShipment.warehouse" id="warehouse">
            <option v-for="warehouse in warehouses" :key="warehouse.id" :value="warehouse">
                {{ warehouse.country }}, {{ warehouse.city }}, {{ warehouse.address }}
            </option>
        </select>
        <br />

        <label for="supplier">Supplier</label>
        <input id="supplier" v-model="warehouseShipment.supplier" type="text" />
        <br />

        <div v-if="editWarehouseShipment">
            <h2>Items to ship</h2>
            <table>
                <th>
                <td>ID</td>
                <td>Book</td>
                <td>Quantity</td>
                <td></td>
                </th>
                <tr :key="i.id" v-for="i in shippedItems">
                    <td>{{ i.id }}</td>
                    <td>{{ ('book' in i) ? i.book.name : "loading ..." }}</td>
                    <td>{{ i.quantity }}</td>
                    <td>
                        <button v-if="warehouseShipment.processed === null" @click="deleteShippedItem($event, i.id)">Delete</button>
                        <button v-else disabled>Delete</button>
                    </td>
                </tr>
                <tr>
                    <td>-</td>
                    <td>
                        <select v-model="newShippedItem.book" id="book">
                            <option v-for="book in books" :key="book.id" :value="book">
                                {{ book.name }}
                            </option>
                        </select>
                    </td>
                    <td>
                        <input @input="validate($event)" id="quantity" v-model.number="newShippedItem.quantity" type="number" />
                    </td>
                </tr>
                <button @click="submitShippedItem">Submit shipped item</button>
            </table>
        </div>

        <button @click="submitWarehouseShipment">
            <p v-if="editWarehouseShipment">Save changes</p>
            <p v-else>Create</p>
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            editWarehouseShipment: false,
            warehouseShipment: {},
            frontendPath: "/warehouse_shipments/",
            backendPath: "/api/warehouse_shipments/",
            warehousesPath: "/api/warehouses/",
            shippedItemsPath: "/api/warehouse_shipped_items/",
            warehouseStoredItemsPath: "/api/warehouse_stored_items/",
            booksPath: "/api/books/",
            warehouses: [],
            books: [],
            shippedItems: [],
            newShippedItem: {}
        }
    },
    async mounted() {
        if (this.$route.path === this.frontendPath + "edit") {
            this.editWarehouseShipment = true
            this.warehouseShipment.id = this.$route.query.warehouseShipmentId
            let response = await fetch(this.backendPath + this.warehouseShipment.id)
            let warehouseShipment = await response.json()
            this.warehouseShipment = warehouseShipment
            await this.fetchInitialWarehouse(this.warehouseShipment)
            await this.fetchShippedItems()
        }
        await this.fetchWarehouses()
        await this.fetchBooks()
    },

    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async submitShippedItem() {
            let shippedItemData = {
                "bookId": this.newShippedItem.book.id,
                "quantity": this.newShippedItem.quantity,
                "warehouseShipmentId": this.warehouseShipment.id
            }
            await window.axios.post(this.shippedItemsPath, shippedItemData);
            this.fetchShippedItems()
        },
        async fetchBooks() {
            let response = await fetch(this.booksPath)
            let data = await response.json()
            this.books = data.data
        },
        async fetchWarehouses() {
            let response = await fetch(this.warehousesPath)
            let data = await response.json()
            this.warehouses = data.data
        },
        async fetchInitialWarehouse(warehouseShipment) {
            let response = await fetch(this.warehousesPath + warehouseShipment.warehouseId)
            let warehouse = await response.json()
            warehouseShipment.warehouse = warehouse
        },
        async fetchShippedItems() {
            let response = await fetch(this.backendPath + this.warehouseShipment.id + "/shipped_items/")
            let data = await response.json()
            this.shippedItems = data.data
            for (let i of data.data) {
                let bookResponse = await fetch(this.booksPath + i.bookId)
                let book = await bookResponse.json()
                i.book = book
            }
        },
        async markShipmentAsArrived() {
            let warehouseShipmentData = {
                "id": this.warehouseShipment.id,
                "created": this.warehouseShipment.created,
                "supplier": this.warehouseShipment.supplier,
                "warehouseId": this.warehouseShipment.warehouseId,
                "arrived": new Date().toISOString()
            }
            await window.axios.put(this.backendPath + this.warehouseShipment.id, warehouseShipmentData);
            let response = await fetch(this.backendPath + this.warehouseShipment.id)
            let warehouseShipment = await response.json()
            this.warehouseShipment = warehouseShipment
            await this.fetchInitialWarehouse(this.warehouseShipment)
        },
        async restoreShipment() {
            let warehouseShipmentData = {
                "id": this.warehouseShipment.id,
                "created": this.warehouseShipment.created,
                "storeId": this.warehouseShipment.storeId,
                "supplier": this.warehouseShipment.supplier,
                "warehouseId": this.warehouseShipment.warehouseId
            }
            await window.axios.put(this.backendPath + this.warehouseShipment.id, warehouseShipmentData);
            let response = await fetch(this.backendPath + this.warehouseShipment.id)
            let warehouseShipment = await response.json()
            this.warehouseShipment = warehouseShipment
            await this.fetchInitialWarehouse(this.warehouseShipment)
        },
        async markShipmentAsProcessed() {
            let warehouseShipmentData = {
                "id": this.warehouseShipment.id,
                "created": this.warehouseShipment.created,
                "warehouseId": this.warehouseShipment.warehouseId,
                "arrived": this.warehouseShipment.arrived,
                "supplier": this.warehouseShipment.supplier,
                "processed": new Date().toISOString(),
            }
            await window.axios.put(this.backendPath + this.warehouseShipment.id, warehouseShipmentData);
            let response = await fetch(this.backendPath + this.warehouseShipment.id)
            let warehouseShipment = await response.json()
            this.warehouseShipment = warehouseShipment
            await this.fetchInitialWarehouse(this.warehouseShipment)
            this.updateWarehouseStoredItems()
        },
        async updateWarehouseStoredItems() {
            for (let shippedItem of this.shippedItems) {
                    let response = await fetch(this.warehouseStoredItemsPath + "/by_book/" + shippedItem.bookId)
                    let warehouseStoredItemsByBookId = (await response.json()).data
                    console.log("by book: ", warehouseStoredItemsByBookId)
                    if (warehouseStoredItemsByBookId.length !== 0 ) {
                        let warehouseStoredItem = warehouseStoredItemsByBookId[0]
                        warehouseStoredItem.quantity = warehouseStoredItem.quantity + shippedItem.quantity
                        await window.axios.put(this.warehouseStoredItemsPath + warehouseStoredItem.id, warehouseStoredItem)
                    } else {
                        let warehouseStoredItem = {
                            "bookId": shippedItem.bookId,
                            "quantity": shippedItem.quantity,
                            "warehouseId": this.warehouseShipment.warehouseId
                        }
                        window.axios.post(this.warehouseStoredItemsPath, warehouseStoredItem)
                    }
                }
        },
        async submitWarehouseShipment() {
            this.warehouseShipment.warehouseId = this.warehouseShipment.warehouse.id
            let warehouseShipmentData = {
                "created": this.warehouseShipment.created,
                "warehouseId": this.warehouseShipment.warehouseId,
                "supplier": this.warehouseShipment.supplier
            }
            if (this.editWarehouseShipment) {
                warehouseShipmentData.id = this.warehouseShipment.id
                await window.axios.put(this.backendPath + this.warehouseShipment.id, warehouseShipmentData);
            } else {
                warehouseShipmentData.created = new Date().toISOString()
                await window.axios.post(this.backendPath, warehouseShipmentData);
            }
            this.$router.push(this.frontendPath)
        },
        async deleteShippedItem(event, itemId) {
            await window.axios.delete(this.shippedItemsPath + itemId)
            this.fetchShippedItems()
        }
    }
}
</script>

<style scoped>
warehouse_shipment_item {
    width: 100em;
    border-width: 1px;
    border-style: solid;
    border-color: gray;
}
</style>