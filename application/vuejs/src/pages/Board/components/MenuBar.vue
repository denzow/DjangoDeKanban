<template>
  <div class="board-menu-bar navbar navbar-dark bg-dark">
    <span class="navbar-brand mb-0 h1">{{ boardName }}</span>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    boardName: {
      type: String,
      default: null,
    },
  },
};
</script>

<style scoped>
.board-menu-bar {
  margin: 1rem 0;
  width: 100%;
}
</style>
