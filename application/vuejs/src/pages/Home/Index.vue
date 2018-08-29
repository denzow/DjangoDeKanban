<template>
  <div class="home">
    <div class="row no-gutters">
      <BoardCard class='board-card col-3' v-for="board in boardList"
                 :title="board.name"
                 :boardId="board.id"
                 :key="board.id" />
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';
import BoardCard from './components/BoardCard.vue';

const { mapState, mapActions } = createNamespacedHelpers('home');


export default {
  name: 'home',
  components: {
    BoardCard,
  },
  computed: {
    ...mapState([
      'boardList',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchBoardList',
    ]),
  },
  async created() {
    this.fetchBoardList();
  },
};
</script>
<style lang="scss" scoped>
  .home {
    padding-top: 1rem;
    align-items: center;
  }
  .board-card {
  }
  .no-gutters {
    margin:1rem;
    padding:0;
    .col,
    [class*="col-"] {
      margin: 0;
      padding:0.5rem 1rem;
    }
  }

</style>
