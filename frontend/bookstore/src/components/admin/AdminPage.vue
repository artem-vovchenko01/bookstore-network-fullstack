<template>
    <div>
        <button @click="backupDb">
            Backup DB
        </button>
        <button @click="restoreDb">
            Restore DB
        </button>
        <button @click="dropDb">
            Drop DB
        </button>
        <br />
    </div>
</template>

<script>
export default {
    data() {
        return {
            item: {},
            frontendPath: "/admin",
            backendPath: "/api/admin",
            editItem: false
        }
    },
    methods: {
        async backupDb() {
          await fetch("http://localhost/api/admin/db_backup")
        },
        async restoreDb() {
          await fetch("http://localhost/api/admin/db_restore")
        },
        async dropDb() {
          await fetch("http://localhost/api/admin/db_drop")
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