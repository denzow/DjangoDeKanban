from django.urls import path
from .consumers import kanban_consumer

urlpatterns = [
    path('ws/boards/<int:board_id>', kanban_consumer.KanbanConsumer)
]
