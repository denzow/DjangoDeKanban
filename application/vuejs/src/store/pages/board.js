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
};

const mutations = {
  setBoardData(state, { boardData }) {
    state.boardData = camelcaseKeys(boardData, { deep: true });
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
