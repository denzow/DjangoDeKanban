from django.urls import path, re_path, include
from .board import BoardListApi

urlpatterns = [
    path('board', BoardListApi.as_view()),
]
