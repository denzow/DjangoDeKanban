<template>
  <div class="board">
    <MenuBar :boardName="kanbanData.name"></MenuBar>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';
import MenuBar from './components/MenuBar.vue';

const { mapState, mapActions } = createNamespacedHelpers('board');


export default {
  name: 'Board',
  components: {
    MenuBar,
  },
  props: {
    boardId: {
      type: Number,
      default: null,
    },
  },
  computed: {
    ...mapState([
      'kanbanData',
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
