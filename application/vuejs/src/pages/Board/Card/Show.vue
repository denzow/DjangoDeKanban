<template>
  <div v-if="fetchFocusedCard" class="modal" aria-labelledby="exampleModalLongTitle" aria-hidden="true" @click="close">
    <div class="modal-dialog" role="document" @click.prevent.stop="">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">{{ focusedCard.title }}</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          {{ focusedCard.content }}
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="close">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapActions } = createNamespacedHelpers('board');


export default {
  props: {
    cardId: {
      type: Number,
      default: null,
    },
    boardId: {
      type: Number,
      default: null,
    },
  },
  name: 'CardShow',
  computed: {
    ...mapState(['focusedCard']),
  },
  methods: {
    close() {
      this.$router.push({
        path: `/boards/${this.boardId}`,
        query: this.$route.query,
      });
    },
    ...mapActions(['fetchFocusedCard']),
  },
  watch: {
    cardId: {
      immediate: true,
      handler(cardId) {
        console.log(cardId);
        this.fetchFocusedCard({
          boardId: this.boardId,
          cardId,
        });
      },
    },
  },
};
</script>

<style lang='scss' scoped>
  .modal {
    display: block;
    background-color: rgba(1, 1, 1, 0.5);
  }
  .modal-dialog {
    z-index: 1060;
  }
</style>
