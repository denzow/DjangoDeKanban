<template>
  <div class="add-pipe-line">
    <nav class="navbar navbar-dark add-pipe-line-button" @click="addPipeLineAction">
      <span class="navbar-brand mb-0 h1">
        Add List(+)
      </span>
    </nav>
  </div>
</template>

<script>

import { createNamespacedHelpers } from 'vuex';

const { mapActions, mapState } = createNamespacedHelpers('board');


export default {
  name: 'AddPipeLine',
  computed: {
    ...mapState([
      'boardData',
    ]),
  },
  methods: {
    addPipeLineAction() {
      const pipeLineName = window.prompt('PipeLineName?');
      if (pipeLineName) {
        this.addPipeLine({
          boardId: this.boardData.boardId,
          pipeLineName,
        });
      }
    },
    ...mapActions([
      'addPipeLine',
    ]),
  },
};
</script>

<style lang='scss' scoped>
  .add-pipe-line {
    margin-right: 1rem;
    width: 15rem;
  }
  .add-pipe-line-button {
    cursor: pointer;
  }
  .navbar {
    background-color: #8c939d;
  }
</style>
