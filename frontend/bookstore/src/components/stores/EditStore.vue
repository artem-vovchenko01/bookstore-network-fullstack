<template>
    <div>
        <label for="item.country">Country</label>
        <input id="country" v-model.trim="item.country" type="text" />
        <br />

        <label for="item.city">City</label>
        <input id="city" v-model.trim="item.city" type="text" />
        <br />

        <label for="item.address">Address</label>
        <input id="address" v-model.trim="item.address" type="text" />
        <br />

        <label for="item.capaciy">Capaciy</label>
        <input id="capaciy" v-model="item.capaciy" type="number" />
        <br />

        <label for="item.worksFrom">Works from</label>
        <input id="worksFrom" v-model="item.worksFrom" type="number" />
        <br />

        <label for="item.worksUntil">Works until</label>
        <input id="worksUntil" v-model="item.worksUntil" type="number" />
        <br />

        <label for="item.workingDays">Working days</label>
        <input id="workingDays" v-model.trim="item.workingDays" type="number" />
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
            frontendPath: "/items",
            backendPath: "/api/items",
            editItem: false
        }
    },
    async mounted() {
        if (this.$route.path === this.frontendPath + "/edit") {
            this.editItem = true
            this.item.id = this.$route.query.itemId
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
                "name": this.item.name,
            }
            if (this.editItem) {
                item.id = this.item.id
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