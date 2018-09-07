<template>
  <div class="board-area">
    <Draggable
      v-model="wrappedPipeLineList"
      class="board-container"
      :options="options"
    >
      <PipeLine
        v-for="pipeLine in wrappedPipeLineList"
        :pipeLine="pipeLine"
        class="pipe-line-item"
        :key="pipeLine.id"
      />
      <AddPipeLine />
    </Draggable>
    <router-view></router-view>
  </div>
</template>

<script>
import Draggable from 'vuedraggable';
import { createNamespacedHelpers } from 'vuex';

import PipeLine from './BoardArea/PipeLine.vue';
import AddPipeLine from './BoardArea/AddPipeLine.vue';

const { mapGetters, mapState, mapActions } = createNamespacedHelpers('board');

export default {
  name: 'BoardArea',
  components: {
    AddPipeLine,
    Draggable,
    PipeLine,
  },
  computed: {
    wrappedPipeLineList: {
      get() {
        return this.getFilteredPipeLineList;
      },
      set(value) {
        console.log(value, this.boardData);
        this.updatePipeLineOrder({
          boardId: this.boardData.boardId,
          pipeLineList: value,
        });
      },
    },
    ...mapGetters([
      'getFilteredPipeLineList',
    ]),
    ...mapState([
      'boardData',
    ]),
  },
  methods: {
    ...mapActions([
      'updatePipeLineOrder',
    ]),
  },
  data() {
    return {
      options: {
        animation: 300,
        draggable: '.pipe-line-item',
      },
    };
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
