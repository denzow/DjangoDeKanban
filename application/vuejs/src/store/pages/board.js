import _ from 'lodash';
import camelcaseKeys from 'camelcase-keys';

import KanbanClient from '@/utils/kanbanClient';


const state = {
  boardData: {
    pipeLineList: [],
  },
  focusedCard: {},
  searchWord: '',
};


const getters = {
  getSocket(state, getters, rootState) {
    return rootState.socket;
  },
  getFilteredPipeLineList(state) {
    const result = [];
    state.boardData.pipeLineList.forEach(pipeline => {
      const clonePipeLine = _.cloneDeep(pipeline);
      clonePipeLine.cardList = clonePipeLine.cardList.map(card => {
        const cloneCard = _.cloneDeep(card);
        const content = cloneCard.content !== null ? cloneCard.content : '';
        if (state.searchWord === null || state.searchWord === '') {
          cloneCard.isShown = true;
        } else {
          cloneCard.isShown = (
            cloneCard.title.toUpperCase().includes(state.searchWord.toUpperCase()) ||
            content.toUpperCase().includes(state.searchWord.toUpperCase())
          );
        }
        return cloneCard;
      });
      result.push(clonePipeLine);
    });
    return result;
  },
  getBoardId(state) {
    return state.boardData.boardId;
  },
};

const actions = {
  initBoard({ getters }, boardId) {
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'init_board',
      boardId,
    });
  },
  broadcastBoardData({ getters }) {
    console.log('call broadcastBoardData');
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'broadcast_board_data',
    });
  },
  setSearchWord({ commit }, searchWord) {
    commit('setSearchWord', searchWord);
  },
  updateCardOrder({ commit, getters }, { pipeLineId, cardList }) {
    console.log(pipeLineId, cardList);
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'update_card_order',
      pipeLineId,
      cardIdList: cardList.map(x => x.cardId),
    });
    commit('updateCardOrder', { pipeLineId, cardList });
  },
  updatePipeLineOrder({ commit, getters }, { boardId, pipeLineList }) {
    console.log(boardId, pipeLineList);
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'update_pipe_line_order',
      boardId,
      pipeLineIdList: pipeLineList.map(x => x.pipeLineId),
    });
    commit('updatePipeLineOrder', { pipeLineList });
  },
  addPipeLine({ getters }, { boardId, pipeLineName }) {
    console.log(boardId, pipeLineName);
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'add_pipe_line',
      boardId,
      pipeLineName,
    });
  },
  addCard({ getters }, { pipeLineId, cardTitle }) {
    console.log(pipeLineId, cardTitle);
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'add_card',
      pipeLineId,
      cardTitle,
    });
  },
  renamePipeLine({ getters }, { pipeLineId, pipeLineName }) {
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'rename_pipe_line',
      pipeLineId,
      pipeLineName,
    });
  },
  deletePipeLine({ getters }, { boardId, pipeLineId }) {
    console.log(boardId, pipeLineId);
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'delete_pipe_line',
      boardId,
      pipeLineId,
    });
  },
  renameBoard({ getters }, { boardId, boardName }) {
    const socket = getters.getSocket;
    socket.sendObj({
      type: 'rename_board',
      boardId,
      boardName,
    });
  },
  async fetchFocusedCard({ commit }, { boardId, cardId }) {
    const cardData = await KanbanClient.getCardData({ boardId, cardId });
    commit('setFocusedCard', cardData);
  },
  async updateCardContent({ commit }, { boardId, cardId, content }) {
    const cardData = await KanbanClient.updateCardData({
      boardId,
      cardId,
      content,
    });
    commit('setFocusedCard', cardData);
  },
  async updateCardTitle({ commit, dispatch }, { boardId, cardId, title }) {
    const cardData = await KanbanClient.updateCardData({
      boardId,
      cardId,
      title,
    });
    commit('setFocusedCard', cardData);
    // titleはボード自体に出ているので他のクライアントへの反映を依頼する必要がある
    dispatch('broadcastBoardData');
  },
  async deleteCard({ dispatch }, { boardId, cardId }) {
    await KanbanClient.deleteCard({
      boardId,
      cardId,
    });
    // カード自体はボード自体に出ているので他のクライアントへの反映を依頼する必要がある
    dispatch('broadcastBoardData');
  },
};

const mutations = {
  setBoardData(state, { boardData }) {
    state.boardData = camelcaseKeys(boardData, { deep: true });
  },
  updateCardOrder(state, { pipeLineId, cardList }) {
    const targetPipeLine = state.boardData.pipeLineList.find(pipeLine => pipeLine.pipeLineId === pipeLineId);
    targetPipeLine.cardList = cardList;
  },
  updatePipeLineOrder(state, { pipeLineList }) {
    state.boardData.pipeLineList = pipeLineList;
  },
  setFocusedCard(state, cardData) {
    state.focusedCard = cardData;
  },
  setSearchWord(state, searchWord) {
    state.searchWord = searchWord;
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
