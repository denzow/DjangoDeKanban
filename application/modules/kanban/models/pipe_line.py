from django.db import models


class PipeLine(models.Model):

    board = models.ForeignKey('kanban.Board', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.board)

    @classmethod
    def get_list_by_board(cls, board):
        return list(cls.objects.filter(board=board).order_by('order'))
