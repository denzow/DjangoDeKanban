from django.urls import path
from django.contrib.auth.decorators import login_required
from .board import BoardListApi, BoardApi


urlpatterns = [
    path('board', login_required(BoardListApi.as_view())),
    path('board/<int:board_id>/', login_required(BoardApi.as_view())),
]
