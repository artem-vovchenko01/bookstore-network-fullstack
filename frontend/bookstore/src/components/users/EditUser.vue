<template>
    <div>
        <img height="50" v-if="user.imageUrl != null" :src="user.imageUrl" alt="Fetched Image" />
        <br />

        <label for="input-file" class="custom-file-upload">Profile picture</label>
        <input id="input-file" class="file-upload-class" type="file" @change="handleFileUpload($event)" />
        <br />

        <label for="username">Username</label>
        <input id="username" v-model.trim="user.username" type="text" />
        <br />

        <label for="password">Password</label>
        <input @input="validate($event)" id="password" v-model.number="user.password" type="password" />
        <br />

        <label for="name">Name</label>
        <input @input="validate($event)" id="name" v-model.number="user.name" type="text" />
        <br />

        <label for="surname">Surname</label>
        <input @input="validate($event)" id="surname" v-model.number="user.surname" type="text" />
        <br />

        <label for="age">Age</label>
        <input @input="validate($event)" id="age" v-model.number="user.age" type="text" />
        <br />

        <label for="email">Email</label>
        <input @input="validate($event)" id="email" v-model.number="user.email" type="text" />
        <br />

        <label for="phone">Phone</label>
        <input @input="validate($event)" id="phone" v-model.number="user.phone" type="text" />
        <br />

        <label for="country">Country</label>
        <input @input="validate($event)" id="country" v-model.number="user.country" type="number" />
        <br />

        <label for="city">City</label>
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
            editUser: false,
            backendPath: "/api/users/",
            frontendPath: "/users/"
        }
    },
    async mounted() {
        if (this.$route.path === "/users/edit") {
            this.editUser = true
            this.user.id = this.$route.query.userId
            let response = await fetch(this.backendPath + this.user.id)
            let user = await response.json()
            this.user = user
            this.fetchImage(user)
        }
    },
    methods: {
        validate(event) {
            console.log("VALIDATING", event)
        },
        async fetchImage(user) {
            let userId = user.id
            try {
                let response = await fetch(this.backendPath + userId + '/profile-pic/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                let blob = await response.blob();
                let url = URL.createObjectURL(blob);
                this.user.imageUrl = url;
                this.user.image = blob;
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        },
        async submitUser() {
            let formData = new FormData();
            formData.append('profile-pic', this.user.image)
            let userData = {
                "name": this.user.name,
                "username": this.user.username,
                "password": this.user.password,
                "surname": this.user.surname,
                "age": this.user.age,
                "email": this.user.email,
                "phone": this.user.phone,
                "country": this.user.country,
                "city": this.user.city
            }
            let responseData = null
            if (this.editUser) {
                userData.id = this.user.id
                responseData = await window.axios.put(this.backendPath + this.user.id, userData, {
                    validateStatus: status => status >= 200
                });
            } else {
                responseData = await window.axios.post(this.backendPath, userData, {
                    validateStatus: status => status >= 200
                });
            }
            let userId = 0;
            if (this.editUser) {
                userId = this.user.id
            } else {
                userId = responseData.data.id;
            }
            await window.axios.post(this.backendPath + userId + "/profile-pic/", formData)
            this.$router.push(this.frontendPath)
        },
        handleFileUpload(event) {
            this.user.image = event.target.files[0]
            let url = URL.createObjectURL(this.user.image);
            this.user.imageUrl = url;
        }
    }
}
</script>

<style scoped>
user_item {
    width: 100em;
    border-width: 1px;
    border-style: solid;
    border-color: gray;
}
</style>