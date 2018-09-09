<template>
  <div class="pipe-line">
    <nav class="navbar navbar-dark">
      <span v-show="!isEditingPipeLineName">
        <span class="navbar-brand mb-0 h1"
              :class="{ 'waiting-rename' : isWaitingRename}"
              @dblclick="startPipeLineNameEdit">{{ pipeLineName }}</span>
        <span class="navbar-brand add-card" data-toggle="tooltip" data-placement="top"
              title="Add Card" @click="addCardAction">
          (+)
        </span>
      </span>
      <span v-show="isEditingPipeLineName">
        <input type="text" v-model="editPipeLineName">
        <button type="button" class="btn btn-primary" @click="savePipeLineName">save</button>
      </span>
    </nav>
    <Draggable
      class="card-container"
      :options="options"
      v-model="wrappedCardList"
      @start="startDragging"
      @end="endDragging"
    >
      <Card v-for="card in wrappedCardList"
            class="item"
            :card="card"
            :key="card.cardId"
      />
    </Draggable>
  </div>
</template>

<script>

import { createNamespacedHelpers } from 'vuex';
import Draggable from 'vuedraggable';
import Card from './Card.vue';

const { mapActions, mapGetters } = createNamespacedHelpers('board');


export default {
  name: 'PipeLine',
  components: {
    Draggable,
    Card,
  },
  props: {
    pipeLine: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      options: {
        group: 'Cards',
        animation: 300,
        draggable: '.item',
      },
      isEditingPipeLineName: false,
      isWaitingRename: false,
      editPipeLineName: '',
    };
  },
  computed: {
    wrappedCardList: {
      get() {
        return this.pipeLine.cardList;
      },
      set(value) {
        console.log(value);
        this.updateCardOrder({
          pipeLineId: this.pipeLine.pipeLineId,
          cardList: value,
        });
      },
    },
    pipeLineName() {
      return this.pipeLine.name;
    },
  },
  watch: {
    pipeLine(newPipeLine, oldPipeLine) {
      if (newPipeLine.name !== oldPipeLine.name) {
        this.isWaitingRename = false;
      }
    },
  },
  methods: {
    startDragging(e) {
      console.log('startDragging', e);
    },
    endDragging(e) {
      console.log('endDragging', e);
    },
    addCardAction() {
      const cardTitle = window.prompt('CardTitle?');
      if (cardTitle) {
        this.addCard({
          pipeLineId: this.pipeLine.pipeLineId,
          cardTitle,
        });
      }
    },
    startPipeLineNameEdit() {
      this.isEditingPipeLineName = true;
      this.editPipeLineName = this.pipeLine.name;
    },
    async savePipeLineName() {
      this.isEditingPipeLineName = false;
      if (this.editPipeLineName === this.pipeLine.name) return;
      await this.renamePipeLine({
        pipeLineId: this.pipeLine.pipeLineId,
        pipeLineName: this.editPipeLineName,
      });
      // リネーム完了までのフラグ
      this.isWaitingRename = true;
    },
    ...mapActions([
      'updateCardOrder',
      'addCard',
      'renamePipeLine',
    ]),
    ...mapGetters([
      'getBoardId',
    ]),
  },
};
</script>

<style lang='scss' scoped>
  .pipe-line {
    margin-right: 1rem;
    width: 15rem;
  }
  .navbar {
    background-color: #6f7180;
  }
  .waiting-rename {
    color: rgba(0, 0, 0, 0.3);
  }
  .card-container {
    height: 100%;
  }
  .add-card {
    cursor: pointer;
  }
</style>
