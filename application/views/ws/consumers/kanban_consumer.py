from channels.db import database_sync_to_async

from modules.kanban import service as kanban_sv

from .base_consumer import BaseJsonConsumer


class KanbanConsumer(BaseJsonConsumer):

    # VueNativeWebSocket経由でStoreにマップするための情報
    namespace = 'board'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board_id = None

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
        await self.send_board_data()

    async def send_board_data(self):
        """
        ボードのデータを送る
        :return:
        """
        kanban_data = await database_sync_to_async(kanban_sv.get_board_data_board_id)(self.board_id)
        await self.send_data({
            'kanbanData': kanban_data,
        }, mutation='setKanbanData')
