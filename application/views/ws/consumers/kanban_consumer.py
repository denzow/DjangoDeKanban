from channels.db import database_sync_to_async

from modules.kanban import service as kanban_sv

from .base_consumer import BaseJsonConsumer


class KanbanConsumer(BaseJsonConsumer):

    # VueNativeWebSocket経由でStoreにマップするための情報
    namespace = 'board'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board_id = None
        self.action_map = {
            'update_card_order': self.update_card_order,
            'update_pipe_line_order': self.update_pipe_line_order,
            'add_pipe_line': self.add_pipe_line,
            'add_card': self.add_card,
            'broadcast_board_data': self.broadcast_board_data,
            'broadcast_board_data_without_requester': self.broadcast_board_data_without_requester,
        }

    async def connect(self):
        if not self.scope['user'].is_authenticated:
            await self.close()
            return
        self.user = self.scope['user']
        self.board_id = self.scope['url_route']['kwargs']['board_id']
        self.room_group_name = self.user.username

        await self.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send_board_data({})

    async def send_board_data(self, event):
        """
        ボードのデータを送る
        :return:
        """
        if event.get('requester_id') == self.consumer_id:
            return
        board_data = await database_sync_to_async(kanban_sv.get_board_data_board_id)(self.board_id)
        await self.send_data({
            'boardData': board_data,
        }, mutation='setBoardData')

    async def update_card_order(self, content):
        """
        ボード内のカードの並び順を更新する
        {
            'type': 'update_card_order',
            'pipeLineId': 1,
            'cardIdList': [3, 1]
        }
        :return:
        """
        pipe_line_id = content['pipeLineId']
        card_id_list = content['cardIdList']
        await database_sync_to_async(kanban_sv.update_card_order)(pipe_line_id, card_id_list)
        await self.broadcast_board_data_without_requester()

    async def update_pipe_line_order(self, content):
        """
        {
            'type': 'update_pipe_line_order',
            'boardId': 1,
            'pipeLineIdList': [2, 1]
        }
        """
        board_id = content['boardId']
        pipe_line_id_list = content['pipeLineIdList']
        await database_sync_to_async(kanban_sv.update_pipe_line_order)(board_id, pipe_line_id_list)
        await self.broadcast_board_data_without_requester()

    async def add_pipe_line(self, content):
        print(content)
        board_id = content['boardId']
        pipe_line_name = content['pipeLineName']
        await database_sync_to_async(kanban_sv.add_pipe_line)(board_id, pipe_line_name)
        await self.broadcast_board_data()

    async def add_card(self, content):
        print(content)
        pipe_line_id = content['pipeLineId']
        card_title = content['cardTitle']
        await database_sync_to_async(kanban_sv.add_card)(pipe_line_id, card_title)
        await self.broadcast_board_data()

    async def broadcast_board_data(self, *args):
        await self.group_send(
            self.room_group_name,
            {
                'type': 'send_board_data',
            }
        )

    async def broadcast_board_data_without_requester(self, *args):
        await self.group_send(
            self.room_group_name,
            {
                'type': 'send_board_data',
                'requester_id': self.consumer_id,
            }
        )
