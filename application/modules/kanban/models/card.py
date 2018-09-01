from django.db import models


class Card(models.Model):

    pipe_line = models.ForeignKey('kanban.PipeLine', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.title, self.pipe_line)

    @classmethod
    def get_list_by_pipe_line(cls, pipe_line):
        return list(cls.objects.filter(pipe_line=pipe_line).order_by('order'))
