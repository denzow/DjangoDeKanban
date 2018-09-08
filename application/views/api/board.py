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


class CardApi(BaseApiView):

    def get(self, _, board_id, card_id):
        card = kanban_sv.get_card_by_card_id(card_id)

        return JsonResponse({
            'card_data': {
                'title': card.title,
                'content': card.content,
                'updated_at': card.updated_at,
            }
        })
