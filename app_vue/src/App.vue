<template>

  <div id="app">

    <Nav/>

    <router-view/>

  </div>

</template>

<style>
@import "assets/css/bootstrap.min.css";
@import "assets/css/style.css";
</style>

<script>
import Nav from "./components/Nav";

export default {
  components: {Nav}
}
</script>
