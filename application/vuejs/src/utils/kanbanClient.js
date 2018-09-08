import axios from 'axios';
import { loadProgressBar } from 'axios-progress-bar';
import camelcaseKeys from 'camelcase-keys';


const _handleSuccess = response => {
  console.log(response.data);
  response.data = camelcaseKeys(response.data, { deep: true });
  return response;
};

class Client {
  constructor() {
    this.service = axios.create();
    this.service.interceptors.response.use(_handleSuccess);
    loadProgressBar({ showSpinner: false }, this.service);
  }

  _get(path, payload) {
    return this.service.get(path, payload);
  }

  _patch(path, payload) {
    return this.service.patch(path, payload);
  }

  _post(path, payload, config = {}) {
    return this.service.post(path, payload, config);
  }

  _put(path, payload) {
    return this.service.put(path, payload);
  }

  _delete(path) {
    return this.service.delete(path);
  }
}


class KanbanClient extends Client {
  constructor() {
    super();
    this.baseUrl = '/api';
  }

  async getBoardList() {
    const response = await this._get(`${this.baseUrl}/boards/`);
    return response.data.boardList;
  }

  async getCardData({ boardId, cardId }) {
    const response = await this._get(`${this.baseUrl}/boards/${boardId}/cards/${cardId}/`);
    return response.data.cardData;
  }
}


export default new KanbanClient();
