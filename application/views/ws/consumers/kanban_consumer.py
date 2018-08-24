from .base_consumer import BaseJsonConsumer


class KanbanConsumer(BaseJsonConsumer):

    async def connect(self):
        self.namespace = 'kanban'
        if not self.scope['user'].is_authenticated:
            await self.close()
            return
        self.user = self.scope['user']
        self.room_group_name = self.user.username

        await self.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send_data({}, action='init')
