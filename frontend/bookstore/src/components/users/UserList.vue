<template>
  <div class="user-list">
    <div class="user" :key="user.id" v-for="user in users">
      <div class="user-profile-picture">
        <img height="50" v-if="user.imageUrl != null" :src="user.imageUrl" alt="Fetched Image" />
      </div>
      <div class="user-info">
        <p class="user-name">Username: {{ user.username }}</p>
        <p>Name: {{ user.name }}</p>
        <p>Surname: {{ user.surname }}</p>
        <p>Age: {{ user.age }}</p>
        <p>Email: {{ user.email }}</p>
        <p>Phone: {{ user.phone }}</p>
        <p>Country: {{ user.country }}</p>
        <p>City: {{ user.city }}</p>
        <p>Item ID: {{ user.id }}</p> -->
        <button @click="deleteUser($event, user.id)">Delete</button>
        <button>
          <router-link :to="{ path: '/users/edit', query: { userId: user.id } }">Edit user</router-link>
        </button>
      </div>
    </div>
  </div>
  <div>
    <div>
      <button>
        <router-link to="/users/create">Add user</router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      imageUrls: {},
      backendPath: "/api/users/",
      frontendPath: "/users/"
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    async deleteUser(event, userId) {
      await window.axios.delete(this.backendPath + userId)
      this.fetchData()
    },
    async fetchData() {
      let response = await fetch(this.backendPath)
      let data = await response.json()
      this.users = data.data
      await this.fetchImages()
    },
    async fetchImages() {
      for (let user of this.users) {
        this.fetchOneImage(user)
      }
    },
    async fetchOneImage(user) {
      let userId = user.id
      try {
        const response = await fetch(this.backendPath + userId + '/profile-pic/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const blob = await response.blob();
        let url = URL.createObjectURL(blob);
        this.imageUrls[userId] = url;
        user.imageUrl = url;
      } catch (error) {
        console.error('Error fetching image:', error);
      }
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

.user-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
}

.user {
  background-color: #F5F5DC; /* Or #F0F0F0 for a cooler tone */
    color: #333333;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.user-profile-picture img {
    width: 100%;
    height: auto;
}

.user-info {
    padding: 10px;
    flex-grow: 1;
}

.user-name {
    font-size: 16px;
    font-weight: bold;
    margin: 0 0 10px 0;
}

.user-price {
    font-size: 14px;
    color: #007bff;
}

</style>