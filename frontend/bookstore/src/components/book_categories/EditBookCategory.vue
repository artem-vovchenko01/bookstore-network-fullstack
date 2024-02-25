<template>
    <div>
        <label for="bookCategory.name">Name</label>
        <input id="name" v-model.trim="bookCategory.name" type="text" />
        <br />

        <button @click="submitBookCategory">
            <p v-if="editBookCategory">Save changes</p>
            <p v-else>Create</p>
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            bookCategory: {},
            editBookCategory: false
        }
    },
    async mounted() {
        if (this.$route.path === "/book_categories/edit") {
            this.editBookCategory = true
            this.bookCategory.id = this.$route.query.bookCategoryId
            let response = await fetch("http://localhost/api/book_categories/" + this.bookCategory.id)
            if (!response.ok) {
                console.log("Error while fetching data!")
            }
            let bookCategory = await response.json()
            this.bookCategory = bookCategory
        }
    },
    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async submitBookCategory() {
            let bookCategoryData = {
                "name": this.bookCategory.name,
            }
            if (this.editBookCategory) {
                bookCategoryData.id = this.bookCategory.id
                await window.axios.put("/api/book_categories/" + this.bookCategory.id, bookCategoryData, {
                    validateStatus: status => status >= 200
                });
            } else {
                await window.axios.post("/api/book_categories/", bookCategoryData, {
                    validateStatus: status => status >= 200
                });
            }
            this.$router.push("/book_categories/")
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