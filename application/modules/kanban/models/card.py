from django.db import models


class Card(models.Model):

    pipe_line = models.ForeignKey('kanban.PipeLine', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.pipe_line)
