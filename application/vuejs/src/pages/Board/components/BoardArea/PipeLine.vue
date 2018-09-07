<template>
  <div class="pipe-line">
    <nav class="navbar navbar-dark">
      <span class="navbar-brand mb-0 h1">{{ pipeLineName }}</span>
      <span class="navbar-brand add-card" data-toggle="tooltip" data-placement="top"
            title="Add Card" @click="addCardAction">
        (+)
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
    ...mapActions([
      'updateCardOrder',
      'addCard',
    ]),
    ...mapGetters([
      'getBoardId',
    ]),
  },
  data() {
    return {
      options: {
        group: 'Cards',
        animation: 300,
        draggable: '.item',
      },
    };
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
  .card-container {
    height: 100%;
  }
  .add-card {
    cursor: pointer;
  }
</style>
