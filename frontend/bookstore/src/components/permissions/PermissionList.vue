<template>
        <div>
            <h2>Permissions</h2>
            <table>
                <th>
                <td>ID</td>
                <td>Resource</td>
                <td>Resource item ID</td>
                <td>Resource item</td>
                <td>Action</td>
                <td>User</td>
                </th>
                <tr :key="i.id" v-for="i in permissions">
                    <td>{{ i.id }}</td>
                    <td>
                    {{
                      i.resourceType === 0 ? "Warehouses" : i.resourceType === 1 ? "Stores" : "not known"
                    }}
                    </td>
                    <td>{{ i.correspondingItemId }}</td>
                    <td>
                      {{ this.itemToString( i.resourceItem ) }} 
                    </td>
                    <td>
                        All (only this option is implemented)
                    </td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td> - </td>
                    <td>
                        <select style="width: 200px; margin 0;" @change="onResourceTypeChange"  v-model="newPermission.resourceTypeStr" id="resourceType">
                            <option v-for="resourceType in resourceTypeOptions" :key="resourceType.getHashCode" :value="resourceType">
                                {{ resourceType }}
                            </option>
                        </select>
                    </td>
                    <td> - </td>
                    <td>
                        <select style="width: 300px;margin 0;" v-if="newPermission.resourceTypeStr === 'Warehouses'" v-model="newPermission.resourceItem" id="resourceItem">
                            <option v-for="resourceItem in warehouses" :key="resourceItem.id" :value="resourceItem">
                                {{ itemToString(resourceItem, 0) }}
                            </option>
                        </select>
                        <div v-else>
                          <select style="width: 300px;margin 0;" v-if="newPermission.resourceTypeStr === 'Stores'" v-model="newPermission.resourceItem" id="resourceItem">
                              <option v-for="resourceItem in stores" :key="resourceItem.id" :value="resourceItem">
                                  {{ itemToString(resourceItem, 1) }}
                              </option>
                          </select>
                          <div v-else>
                            <p>Choose resource type first</p>
                            <select style="margin 0;" disabled></select>
                          </div>
                        </div>
                    </td>
                    <td>
                        All actions (the only option implemented for now)
                    </td>
                    <td>
                        <select v-model="newPermission.user" id="user">
                            <option v-for="user in users" :key="user.id" :value="user">
                                {{ user.name + " " + user.surname }}
                            </option>
                        </select>
                    </td>
                </tr>
                <button @click="submitPermission">Submit new permission</button>
            </table>
        </div>
</template>

<script>
export default {
  data() {
    return {
      newPermission: {},
      users: [],
      warehouses: [],
      stores: [],
      items: [],
      frontendPath: "/permissions/",
      backendPath: "/api/permissions/",
      warehousesPath: "/api/warehouses/",
      storesPath: "/api/stores/",
      usersPath: "/api/users/",
      resourceTypes: [0, 1],
      resourceTypeOptions: ["Warehouses", "Stores"]
    }
  },
  async mounted() {
    await this.fetchData()
    await this.fetchUsers()
    await this.fetchWarehouses()
    await this.fetchStores()
  },
  methods: {
    async submitPermission() {
        let permissionData = {
            "resourceType": this.newPermission.resourceTypeStr === "Warehouses" ? 0 : 1,
            "correspondingItemId": this.newPermission.resourceItem.id,
            "allowedAction": 0,
            "userId": this.newPermission.user.id
        }
        await window.axios.post(this.backendPath, permissionData);
        this.$router.push(this.frontendPath)
    },
    async onResourceTypeChange() {

    },
    async deletePermission(event, itemId) {
        await window.axios.delete(this.backendPath + itemId)
        await this.fetchData()
    },
    itemToString(item, resourceTypeId) {
      if (resourceTypeId === 0) {
        return item.country + ", " + item.city + ", " + item.address
      } else {
        if (resourceTypeId === 1) {
            return item.country + ", " + item.city + ", " + item.address
          }
          else {
            return "cant get string representation"
          }
        }
      },
    async fetchData() {
      let response = await fetch(this.backendPath)
      let data = await response.json()
      this.permissions = data.data
      for (let permission of this.permissions) {
        let resources = this.permissions.resourceType === 0 ? this.warehouses : this.stores
        let resource = resources.filter(r => r.id === permission.correspondingItemId)[0]
        permission.resourceItem = resource
      }
    },
    async fetchUsers() {
      let responseUsers = await fetch(this.usersPath)
      let dataUsers = await responseUsers.json()
      this.users = dataUsers.data
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