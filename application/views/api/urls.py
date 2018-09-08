from django.urls import path
from django.contrib.auth.decorators import login_required
from .board import BoardListApi, BoardApi, CardApi


urlpatterns = [
    path('boards/', login_required(BoardListApi.as_view())),
    path('boards/<int:board_id>/', login_required(BoardApi.as_view())),
    path('boards/<int:board_id>/cards/<int:card_id>/', login_required(CardApi.as_view())),
]
