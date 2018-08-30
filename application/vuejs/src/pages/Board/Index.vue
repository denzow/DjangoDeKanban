<template>
  <div class="board">
    <MenuBar :boardName="boardData.name"></MenuBar>
    <BoardArea></BoardArea>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';
import MenuBar from './components/MenuBar.vue';
import BoardArea from './components/BoardArea.vue';

const { mapState, mapActions } = createNamespacedHelpers('board');


export default {
  name: 'Board',
  components: {
    MenuBar,
    BoardArea,
  },
  props: {
    boardId: {
      type: Number,
      default: null,
    },
  },
  computed: {
    ...mapState([
      'boardData',
    ]),
  },
  methods: {
    ...mapActions([
      'initBoard',
    ]),
  },
  watch: {
    boardId: {
      immediate: true,
      handler(boardId) {
        console.log(boardId);
      },
    },
  },
};
</script>
<style lang="scss" scoped>
</style>
