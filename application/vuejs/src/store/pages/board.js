// import KanbanClient from '@/utils/kanbanClient';
import camelcaseKeys from 'camelcase-keys';


const state = {
  kanbanData: {},
};


const getters = {
  getSocket(state, getters, rootState) {
    return rootState.socket;
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
  setKanbanData(state, { kanbanData }) {
    state.kanbanData = camelcaseKeys(kanbanData, { deep: true });
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
