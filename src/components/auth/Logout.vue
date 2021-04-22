<template>
  <div class="log"></div>
</template>

<script>
export default {
    name:"Logout",
    created(){
        this.$store.dispatch('Logout')
    }
}
</script>

<style>

</style>