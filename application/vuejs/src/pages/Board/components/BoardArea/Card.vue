<template>
  <div class="card" @click="openCard">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
    </div>
  </div>
</template>

<script>

import { createNamespacedHelpers } from 'vuex';

const { mapGetters } = createNamespacedHelpers('board');
export default {
  name: 'Card',
  props: {
    card: {
      type: Object,
      default: () => {},
    },
  },
  computed: {
    title() {
      return this.card.title;
    },
    content() {
      return this.card.content;
    },
    ...mapGetters(['getBoardId']),
  },
  methods: {
    openCard() {
      console.log('OPEN');
      this.$router.push({
        path: `/boards/${this.getBoardId}/cards/${this.card.cardId}`,
        query: this.$route.query,
      });
    },
  },
};
</script>

<style lang='scss' scoped>
  .card {
    margin-bottom: 0.2rem;
    cursor: pointer;
  }
</style>
