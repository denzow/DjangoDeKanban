from django.http import JsonResponse

from modules.kanban import service as kanban_sv
from .base import BaseApiView


class BoardListApi(BaseApiView):

    def get(self, _):
        board_list = []
        for board in kanban_sv.get_board_list_by_owner(self.login_member):
            board_list.append({
                'id': board.id,
                'name': board.name,
            })
        return JsonResponse({
            'board_list': board_list,
        })


class BoardApi(BaseApiView):

    def get(self, _, board_id):
        board_data = kanban_sv.get_board_data_board_id(board_id)

        return JsonResponse({
            'board_data': board_data,
        })



