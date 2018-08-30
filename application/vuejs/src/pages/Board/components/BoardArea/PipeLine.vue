<template>
  <div class="pipe-line">
    <nav class="navbar navbar-dark">
      <span class="navbar-brand mb-0 h1">{{ pipeLineName }}</span>
    </nav>
    <draggable
      :options="options"
      v-model="wrappedCardList"
      @start="startDragging"
      @end="endDragging"
    >
    <Card v-for="card in wrappedCardList"
          :card="card"
          :key="card.id"
    />
    </draggable>
  </div>
</template>

<script>
import Draggable from 'vuedraggable';
import Card from './Card.vue';


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
  },
  data() {
    return {
      options: {
        group: 'kanban',
        animation: 300,
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
</style>
