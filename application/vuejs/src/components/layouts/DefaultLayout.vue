<template>
  <div>
    <MyHeader></MyHeader>
    <div class="container-fluid">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import MyHeader from './MyHeader.vue';

export default {
  name: 'DefaultLayout',
  components: {
    MyHeader,
  },
};
</script>

<style scoped>
</style>
