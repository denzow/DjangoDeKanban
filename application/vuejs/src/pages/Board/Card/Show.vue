<template>
  <div class="modal" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          AAAAAAAAAAAAAAAAAAAAAA
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
  methods: {
    close() {
      this.$router.push({
        path: `/board/${this.boardId}`,
        query: this.$route.query,
      });
    },
  },
  watch: {
    cardId: {
      immediate: true,
      handler(cardId) {
        console.log(cardId);
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
