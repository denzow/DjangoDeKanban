from django.urls import path
from django.contrib.auth.decorators import login_required
from .accounts import AccountsApi
from .boards import BoardListApi, CardApi


urlpatterns = [
    path('accounts/', login_required(AccountsApi.as_view())),
    path('boards/', login_required(BoardListApi.as_view())),
    path('boards/<int:board_id>/cards/<int:card_id>/', login_required(CardApi.as_view())),
]
