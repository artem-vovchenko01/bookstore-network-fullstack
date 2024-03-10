<template>
    <div>
        <img height="50" v-if="user.imageUrl != null" :src="user.imageUrl" alt="Fetched Image" />
        <br />

        <label for="input-file" class="custom-file-upload">Profile picture</label>
        <input id="input-file" class="file-upload-class" type="file" @change="handleFileUpload($event)" />
        <br />

        <label for="name">Username</label>
        <input id="username" v-model.trim="user.username" type="text" />
        <br />

        <label for="user.password">Password</label>
        <input @input="validate($event)" id="password" v-model.number="user.password" type="password" />
        <br />

        <label for="description">Name</label>
        <input @input="validate($event)" id="name" v-model.number="user.name" type="text" />
        <br />

        <label for="surname">Surname</label>
        <input @input="validate($event)" id="surname" v-model.number="user.surname" type="text" />
        <br />

        <label for="user.age">Age</label>
        <input @input="validate($event)" id="age" v-model.number="user.age" type="text" />
        <br />

        <label for="user.email">Email</label>
        <input @input="validate($event)" id="email" v-model.number="user.email" type="text" />
        <br />

        <label for="user.phone">Phone</label>
        <input @input="validate($event)" id="phone" v-model.number="user.phone" type="text" />
        <br />

        <label for="user.country">Country</label>
        <input @input="validate($event)" id="country" v-model.number="user.country" type="number" />
        <br />

        <label for="user.city">City</label>
        <input @input="validate($event)" id="city" v-model.number="user.city" type="number" />
        <br />

        <button @click="submitUser">
            {{ editUser ? "Save changes" : "Create" }}                
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {},
            imageUrls: {},
            editUser: false,
            backendPath: "/api/users/",
            frontendPath: "/users/"
        }
    },
    async mounted() {
        await this.fetchBookCategories()
        if (this.$route.path === "/users/edit") {
            this.editUser = true
            this.user.id = this.$route.query.bookId
            let response = await fetch(this.backendPath + this.user.id)
            let user = await response.json()
            this.user = user
            await this.fetchInitialCategory(user)
            this.fetchImage(user)
        }
    },
    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async fetchBookCategories() {
            let response = await fetch("http://localhost/api/book_categories/")
            let data = await response.json()
            this.bookCategories = data.data
        },
        async fetchInitialCategory(user) {
            let response = await fetch("http://localhost/api/book_categories/" + user.categoryId)
            let category = await response.json()
            user.category = category
        },
        async fetchImage(user) {
            let user = user.id
            try {
                let response = await fetch(this.backendPath + bookId + '/cover/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                let blob = await response.blob();
                let url = URL.createObjectURL(blob);
                this.imageUrls[bookId] = url;
                this.user.imageUrl = url;
                this.user.image = blob;
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        },
        async submitBook() {
            let formData = new FormData();
            formData.append('cover', this.user.image)
            let bookData = {
                "name": this.user.name,
                "description": this.user.description,
                "categoryId": this.user.category.id,
                "author": this.user.author,
                "pages": this.user.pages,
                "publisher": this.user.publisher,
                "type": this.user.type,
                "lang": this.user.lang,
                "year": this.user.year
            }
            let responseData = null
            if (this.editUser) {
                bookData.id = this.user.id
                responseData = await window.axios.put(this.backendPath + this.user.id, bookData, {
                    validateStatus: status => status >= 200
                });
            } else {
                responseData = await window.axios.post(this.backendPath, bookData, {
                    validateStatus: status => status >= 200
                });
            }
            let bookId = 0;
            if (this.editBook) {
                bookId = this.user.id
            } else {
                bookId = responseData.data.id;
            }
            await window.axios.post(this.backendPath + bookId + "/cover/", formData)
            this.$router.push(this.frontendPath)
        },
        handleFileUpload(event) {
            this.user.image = event.target.files[0]
            let url = URL.createObjectURL(this.user.image);
            this.imageUrls[this.user.id] = url;
            this.user.imageUrl = url;
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