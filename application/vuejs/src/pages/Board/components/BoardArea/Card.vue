<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
    </div>
  </div>
</template>

<script>

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
  },
};
</script>

<style lang='scss' scoped>
  .card {
    margin-bottom: 0.2rem;
  }
</style>
