<template>
  <div class="board-menu-bar navbar navbar-expand-lg navbar-light bg-light">
    {{ boardName }}
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
