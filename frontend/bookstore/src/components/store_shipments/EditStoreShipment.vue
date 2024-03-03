<template>
    <div>
        <button @click="restoreShipment()">Restore shipment</button>
        <button v-if="storeShipment.processed === null" @click="cancelShipment()">Cancel shipment</button>
        <button v-if="storeShipment.departed === null" @click="markShipmentAsDeparted()">Shipment departed from warehouse</button>
        <button v-if="storeShipment.arrived === null && storeShipment.departed !== null" @click="markShipmentAsArrived()">Shipment arrived to the store</button>
        <button v-if="storeShipment.processed === null && storeShipment.arrived !== null" @click="markShipmentAsProcessed()">Shipment was processed in the store</button>
        <label for="warehouse">Warehouse</label>
        <select v-model="storeShipment.warehouse" id="warehouse">
            <option v-for="warehouse in warehouses" :key="warehouse.id" :value="warehouse">
                {{ warehouse.country }}, {{ warehouse.city }}, {{ warehouse.address }}
            </option>
        </select>
        <br />

        <label for="store">Store</label>
        <select v-model="storeShipment.store" id="store">
            <option v-for="store in stores" :key="store.id" :value="store">
                {{ store.country }}, {{ store.city }}, {{ store.address }}
            </option>
        </select>
        <br />

        <div v-if="editStoreShipment">
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
                        <button v-if="storeShipment.departed === null" @click="deleteShippedItem($event, i.id)">Delete</button>
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
                <button v-if="storeShipment.departed === null" @click="submitShippedItem">Submit shipped item</button>
            </table>
        </div>

        <button @click="submitStoreShipment">
            <p v-if="editStoreShipment">Save changes</p>
            <p v-else>Create</p>
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            editStoreShipment: false,
            storeShipment: {},
            frontendPath: "/store_shipments/",
            backendPath: "/api/store_shipments/",
            storesPath: "/api/stores/",
            warehousesPath: "/api/warehouses/",
            shippedItemsPath: "/api/store_shipped_items/",
            storeStoredItemsPath: "/api/store_stored_items/",
            booksPath: "/api/books/",
            books: [],
            shippedItems: [],
            newShippedItem: {},
            warehouses: [],
            stores: []
        }
    },
    async mounted() {
        if (this.$route.path === this.frontendPath + "edit") {
            this.editStoreShipment = true
            this.storeShipment.id = this.$route.query.storeShipmentId
            let response = await fetch(this.backendPath + this.storeShipment.id)
            let storeShipment = await response.json()
            this.storeShipment = storeShipment
            await this.fetchInitialStore(this.storeShipment)
            await this.fetchInitialWarehouse(this.storeShipment)
            await this.fetchShippedItems()
            console.log("cur shipment:" ,this.storeShipment)
        }
        await this.fetchStores()
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
                "storeShipmentId": this.storeShipment.id
            }
            await window.axios.post(this.shippedItemsPath, shippedItemData);
            this.fetchShippedItems()
        },
        async fetchBooks() {
            let response = await fetch(this.booksPath)
            let data = await response.json()
            this.books = data.data
        },
        async fetchStores() {
            let response = await fetch(this.storesPath)
            let data = await response.json()
            this.stores = data.data
        },
        async fetchWarehouses() {
            let response = await fetch(this.warehousesPath)
            let data = await response.json()
            this.warehouses = data.data
        },
        async fetchInitialStore(storeShipment) {
            let response = await fetch(this.storesPath + storeShipment.storeId)
            let store = await response.json()
            storeShipment.store = store
        },
        async fetchInitialWarehouse(storeShipment) {
            let response = await fetch(this.warehousesPath + storeShipment.warehouseId)
            let warehouse = await response.json()
            storeShipment.warehouse = warehouse
        },
        async fetchShippedItems() {
            let response = await fetch(this.backendPath + this.storeShipment.id + "/shipped_items/")
            let data = await response.json()
            this.shippedItems = data.data
            for (let i of this.shippedItems) {
                let bookResponse = await fetch(this.booksPath + i.bookId)
                let book = await bookResponse.json()
                i.book = book
            }
        },
        async submitStoreShipment() {
            this.storeShipment.storeId = this.storeShipment.store.id
            this.storeShipment.warehouseId = this.storeShipment.warehouse.id
            let storeShipmentData = {
                "created": this.storeShipment.created,
                "storeId": this.storeShipment.storeId,
                "warehouseId": this.storeShipment.warehouseId,
            }
            if (this.editStoreShipment) {
                storeShipmentData.id = this.storeShipment.id
                await window.axios.put(this.backendPath + this.storeShipment.id, storeShipmentData);
            } else {
                storeShipmentData.created = new Date().toISOString()
                await window.axios.post(this.backendPath, storeShipmentData);
            }
            this.$router.push(this.frontendPath)
        },
        async markShipmentAsDeparted() {
            let storeShipmentData = {
                "id": this.storeShipment.id,
                "created": this.storeShipment.created,
                "storeId": this.storeShipment.storeId,
                "warehouseId": this.storeShipment.warehouseId,
                "departed": new Date().toISOString()
            }
            await window.axios.put(this.backendPath + this.storeShipment.id, storeShipmentData);
            let response = await fetch(this.backendPath + this.storeShipment.id)
            let storeShipment = await response.json()
            this.storeShipment = storeShipment
            await this.fetchInitialStore(this.storeShipment)
            await this.fetchInitialWarehouse(this.storeShipment)
        },
        async markShipmentAsArrived() {
            let storeShipmentData = {
                "id": this.storeShipment.id,
                "created": this.storeShipment.created,
                "storeId": this.storeShipment.storeId,
                "warehouseId": this.storeShipment.warehouseId,
                "departed": this.storeShipment.departed,
                "arrived": new Date().toISOString()
            }
            await window.axios.put(this.backendPath + this.storeShipment.id, storeShipmentData);
            let response = await fetch(this.backendPath + this.storeShipment.id)
            let storeShipment = await response.json()
            this.storeShipment = storeShipment
            await this.fetchInitialStore(this.storeShipment)
            await this.fetchInitialWarehouse(this.storeShipment)
        },
        async restoreShipment() {
            let storeShipmentData = {
                "id": this.storeShipment.id,
                "created": this.storeShipment.created,
                "storeId": this.storeShipment.storeId,
                "warehouseId": this.storeShipment.warehouseId
            }
            await window.axios.put(this.backendPath + this.storeShipment.id, storeShipmentData);
            let response = await fetch(this.backendPath + this.storeShipment.id)
            let storeShipment = await response.json()
            this.storeShipment = storeShipment
            await this.fetchInitialStore(this.storeShipment)
            await this.fetchInitialWarehouse(this.storeShipment)
        },
        async markShipmentAsProcessed() {
            let storeShipmentData = {
                "id": this.storeShipment.id,
                "created": this.storeShipment.created,
                "storeId": this.storeShipment.storeId,
                "warehouseId": this.storeShipment.warehouseId,
                "departed": this.storeShipment.departed,
                "arrived": this.storeShipment.arrived,
                "processed": new Date().toISOString(),
            }
            await window.axios.put(this.backendPath + this.storeShipment.id, storeShipmentData);
            let response = await fetch(this.backendPath + this.storeShipment.id)
            let storeShipment = await response.json()
            this.storeShipment = storeShipment
            await this.fetchInitialStore(this.storeShipment)
            await this.fetchInitialWarehouse(this.storeShipment)
            this.updateStoreStoredItems()
        },
        async updateStoreStoredItems() {
            for (let shippedItem of this.shippedItems) {
                    let response = await fetch(this.storeStoredItemsPath + "/by_book/" + shippedItem.bookId)
                    let storeStoredItemsByBookId = (await response.json()).data
                    console.log("by book: ", storeStoredItemsByBookId)
                    if (storeStoredItemsByBookId.length !== 0 ) {
                        let storeStoredItem = storeStoredItemsByBookId[0]
                        storeStoredItem.quantity = storeStoredItem.quantity + shippedItem.quantity
                        await window.axios.put(this.storeStoredItemsPath + storeStoredItem.id, storeStoredItem)
                    } else {
                        let storeStoredItem = {
                            "bookId": shippedItem.bookId,
                            "quantity": shippedItem.quantity,
                            "storeId": this.storeShipment.storeId
                        }
                        window.axios.post(this.storeStoredItemsPath, storeStoredItem)
                    }
                }
        },
        async deleteShippedItem(event, itemId) {
            await window.axios.delete(this.shippedItemsPath + itemId)
            this.fetchShippedItems()
        },
        async cancelShipment() {
            await window.axios.delete(this.backendPath + this.storeShipment.id)
            this.$router.push(this.frontendPath)
        }
    }
}
</script>

<style scoped>
store_shipment_item {
    width: 100em;
    border-width: 1px;
    border-style: solid;
    border-color: gray;
}
</style>