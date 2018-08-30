<template>
  <div class="board-area">
    <Draggable
      v-model="wrappedPipeLineList"
      class="board-container"
    >
      <PipeLine
        v-for="pipeLine in wrappedPipeLineList"
        :pipeLine="pipeLine"
        :key="pipeLine.id"
      />
    </Draggable>
  </div>
</template>

<script>
import Draggable from 'vuedraggable';
import { createNamespacedHelpers } from 'vuex';

import PipeLine from './BoardArea/PipeLine.vue';

const { mapGetters } = createNamespacedHelpers('board');

export default {
  name: 'BoardArea',
  components: {
    Draggable,
    PipeLine,
  },
  props: {
    boardData: {
      type: Object,
      default: () => {},
    },
  },
  computed: {
    wrappedPipeLineList: {
      get() {
        return this.getFilteredPipeLineList;
      },
      set(value) {
        console.log(value);
      },
    },
    ...mapGetters([
      'getFilteredPipeLineList',
    ]),
  },
};
</script>

<style scoped>
.board-area {
  margin: 1rem 0;
  width: 100%;
}
.board-container {
  display: flex;
}
</style>
