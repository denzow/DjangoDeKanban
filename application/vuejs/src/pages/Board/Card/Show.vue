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
        <div class="modal-body" v-show="!isEditing">
          <p v-if="focusedCard.content" @dblclick="startEdit" class="card-content">{{ focusedCard.content }}</p>
          <p v-else @click="startEdit" class="empty-content">enter content.</p>
        </div>
        <div class="modal-body" v-show="isEditing">
          <textarea class="edit-area" v-model="editContent"></textarea>
          <button type="button" class="btn btn-primary" @click="saveContent">Save</button>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="close">Close</button>
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
  data() {
    return {
      isEditing: false,
      editContent: '',
    };
  },
  methods: {
    close() {
      this.$router.push({
        path: `/boards/${this.boardId}`,
        query: this.$route.query,
      });
    },
    startEdit() {
      this.isEditing = true;
      this.editContent = this.focusedCard.content;
    },
    async saveContent() {
      this.isEditing = false;
      await this.updateCardContent({
        boardId: this.boardId,
        cardId: this.cardId,
        content: this.editContent,
      });
    },
    ...mapActions([
      'fetchFocusedCard',
      'updateCardContent',
    ]),
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
  .edit-area {
    width: 95%;
    height: 5rem;
  }
  .empty-content {
    text-decoration: underline;
    cursor: pointer;
  }
  .card-content {
    white-space: pre;
  }
</style>
