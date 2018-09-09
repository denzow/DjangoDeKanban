<template>
  <div class="board">
    <MenuBar></MenuBar>
    <BoardArea></BoardArea>
  </div>
</template>

<script>
import MenuBar from './components/MenuBar.vue';
import BoardArea from './components/BoardArea.vue';


export default {
  name: 'Board',
  components: {
    MenuBar,
    BoardArea,
  },
};
</script>
<style lang="scss" scoped>
</style>
