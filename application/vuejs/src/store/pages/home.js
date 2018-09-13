import KanbanClient from '@/utils/kanbanClient';


const state = {
  boardList: [],
};

const actions = {
  async fetchBoardList({ commit }) {
    const boardList = await KanbanClient.getBoardList();
    commit('setBoardList', { boardList });
  },
  async addBoard({ dispatch }, { boardName }) {
    await KanbanClient.addBoard({ boardName });
    dispatch('fetchBoardList');
  },
};

const mutations = {
  setBoardList(state, { boardList }) {
    state.boardList = boardList;
  },
};


export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
