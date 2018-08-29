<template>
  <div class="board">
    {{boardId}}
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapActions } = createNamespacedHelpers('board');


export default {
  name: 'Board',
  props: {
    boardId: {
      type: Number,
      default: null,
    },
  },
  components: {
  },
  computed: {
  },
  methods: {
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
