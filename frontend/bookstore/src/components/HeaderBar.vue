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
        <router-link to="/profile">Profile</router-link>
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
  .header ul {
    background-color: #2c3e50;
    margin: 0;
    padding: 0;
    list-style-type: none;
  }
  .header li {
    margin: 1rem;
    float: left;
    list-style-type: none;
  }
  nav {
    width: 100%;
    display: block;
  }
</style>
