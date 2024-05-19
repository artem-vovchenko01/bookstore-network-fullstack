<template>
  <div class="header">
    <nav>
      <ul>
        <li>
        <router-link to="/news">News</router-link>
        </li>
        <li>
        <router-link to="/books">Books</router-link>
        </li>
        <li>
        <router-link to="/book_categories">Book categories</router-link>
        </li>
        <li>
        <router-link to="/stores">Stores</router-link>
        </li>
        <li>
        <router-link to="/store_stored_items">Store items</router-link>
        </li>
        <li>
        <router-link to="/warehouses">Warehouses</router-link>
        </li>
        <li>
        <router-link to="/warehouse_stored_items">Warehouse items</router-link>
        </li>
        <li>
        <router-link to="/store_shipments">Store shipments</router-link>
        </li>
        <li>
        <router-link to="/warehouse_shipments">Warehouse shipments</router-link>
        </li>
        <li>
        <router-link to="/cart">Cart</router-link>
        </li>
        <li>
        <router-link to="/permissions">Permissions</router-link>
        </li>
        <li>
        <router-link to="/users">Usrs</router-link>
        </li>
        <li>
        <router-link to="/profile">Prfl</router-link>
        </li>
        <li>
        <router-link to="/admin">Admin</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  props: {
    msg: String
  }
}
</script>

<style scoped>
a.router-link-active {
  color: yellow;
}
.header {
    padding: 10px 20px;
    background-color: #003366;
    color: #FFFFFF;
    text-align: center; /* Ensures text and inline-elements are centered */
}

nav {
  display: inline-block; /* Makes the nav container inline for text-align to affect it */
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center; /* Centers flex items on the main axis */
}

nav ul li {
    margin-right: 20px;
}

nav ul li:last-child {
    margin-right: 0;
}
</style>
