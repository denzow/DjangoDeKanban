import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from modules.kanban import service as kanban_sv
from .base import BaseApiView


@method_decorator(csrf_exempt, name='dispatch')
class BoardListApi(BaseApiView):

    def get(self, _):
        """
        ボードの一覧を戻す
        """
        board_list = []
        for board in kanban_sv.get_board_list_by_owner(self.login_member):
            board_list.append({
                'id': board.id,
                'name': board.name,
            })
        return JsonResponse({
            'board_list': board_list,
        })

    def post(self, request):
        """
        新しいボードを追加する
        """
        data = json.loads(request.body)
        board_name = data.get('boardName')
        board = kanban_sv.add_board(
            owner=self.login_member,
            board_name=board_name
        )
        return JsonResponse({
            'board_data': {
                'id': board.id,
                'name': board.name,
            }
        })


@method_decorator(csrf_exempt, name='dispatch')
class CardApi(BaseApiView):

    def get(self, _, board_id, card_id):
        """
        カードを追加する
        """
        card = kanban_sv.get_card_by_card_id(card_id)

        return JsonResponse({
            'card_data': {
                'title': card.title,
                'content': card.content,
                'updated_at': card.updated_at,
            }
        })

    def patch(self, request, board_id, card_id):
        """
        カードの内容を更新する
        """
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        card = kanban_sv.update_card(card_id=card_id, title=title, content=content)

        return JsonResponse({
            'card_data': {
                'title': card.title,
                'content': card.content,
                'updated_at': card.updated_at,
            }
        })

    def delete(self, _, board_id, card_id):
        """
        カードを削除する
        """
        kanban_sv.delete_card(card_id=card_id)
        return JsonResponse({
            'success': True
        })