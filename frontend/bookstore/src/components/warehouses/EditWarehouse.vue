<template>
    <div>
        <label for="country">Country</label>
        <input id="country" v-model.trim="item.country" type="text" />
        <br />

        <label for="city">City</label>
        <input id="city" v-model.trim="item.city" type="text" />
        <br />

        <label for="address">Address</label>
        <input id="address" v-model.trim="item.address" type="text" />
        <br />

        <label for="capacity">Capacity</label>
        <input id="capacity" v-model="item.capacity" type="number" />
        <br />

        <button @click="submitItem">
            <p v-if="editItem">Save changes</p>
            <p v-else>Create</p>
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            item: {},
            frontendPath: "/warehouses",
            backendPath: "/api/warehouses",
            editItem: false
        }
    },
    async mounted() {
        if (this.$route.path === this.frontendPath + "/edit") {
            this.editItem = true
            this.item.id = this.$route.query.warehouseId
            let response = await fetch(this.backendPath + "/" + this.item.id)
            let item = await response.json()
            this.item = item
        }
    },
    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async submitItem() {
            let itemData = {
                "country": this.item.country,
                "city": this.item.city,
                "address": this.item.address,
                "capacity": this.item.capacity,
                "utilization": 0
            }
            if (this.editItem) {
                itemData.id = this.item.id
                await window.axios.put(this.backendPath + "/" + this.item.id, itemData, {
                    validateStatus: status => status >= 200
                });
            } else {
                await window.axios.post(this.backendPath + "/", itemData, {
                    validateStatus: status => status >= 200
                });
            }
            this.$router.push(this.frontendPath + "/")
        }
    }
}
</script>

<style scoped>
book_category_item {
    width: 100em;
    border-width: 1px;
    border-style: solid;
    border-color: gray;
}
</style>