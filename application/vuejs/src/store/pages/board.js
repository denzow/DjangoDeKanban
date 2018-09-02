// import KanbanClient from '@/utils/kanbanClient';
import camelcaseKeys from 'camelcase-keys';


const state = {
  boardData: {
    pipeLineList: [],
  },
};


const getters = {
  getSocket(state, getters, rootState) {
    return rootState.socket;
  },
  getFilteredPipeLineList(state) {
    return state.boardData.pipeLineList;
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
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
