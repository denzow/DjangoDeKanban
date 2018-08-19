from django.db import models


class PipeLine(models.Model):

    board = models.ForeignKey('kanban.Board', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.board)
