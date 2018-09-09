import KanbanClient from '@/utils/kanbanClient';


const state = {
  accountInfo: null,
};

const actions = {
  async fetchAccountInfo({ commit }) {
    const accountInfo = await KanbanClient.getAccountInfo();
    commit('setAccountInfo', accountInfo);
  },
};

const mutations = {
  setAccountInfo(state, accountInfo) {
    state.accountInfo = accountInfo;
  },
};


export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
