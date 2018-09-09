<template>
  <div class="board-menu-bar navbar navbar-dark bg-dark">
    <span class="navbar-brand mb-0 h1">{{ boardName }}</span>
      <nav class="my-2 my-md-0 mr-md-3">
        <form class="form-inline mt-2 mt-md-0" id="search-form">
          <input name="query" v-model="wrappedSearchWord" class="form-control mr-3"
                 type="text" placeholder="Search" aria-label="Search">
        </form>
      </nav>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

const { mapActions, mapState } = createNamespacedHelpers('board');


export default {
  name: 'MenuBar',
  props: {
    boardName: {
      type: String,
      default: null,
    },
  },
  computed: {
    wrappedSearchWord: {
      get() {
        return this.searchWord;
      },
      set(val) {
        this.setSearchWord(val);
      },
    },
    ...mapState(['searchWord']),
  },
  methods: {
    ...mapActions(['setSearchWord']),
  },
};
</script>

<style scoped>
.board-menu-bar {
  margin: 1rem 0;
  width: 100%;
}
</style>
