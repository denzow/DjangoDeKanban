from django.http import JsonResponse
from .base import BaseApiView


class AccountsApi(BaseApiView):

    def get(self, _):
        account = self.login_member
        if account.is_authenticated:
            return JsonResponse({
                'account_info': {
                    'account_id': account.id,
                    'name': account.username,
                }
            })

        return JsonResponse({
            'account_info': None,
        })
