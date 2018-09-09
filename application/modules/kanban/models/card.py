from django.db import models


class Card(models.Model):

    pipe_line = models.ForeignKey('kanban.PipeLine', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.title, self.pipe_line)

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_by_id(cls, card_id):
        try:
            return cls.objects.get(id=card_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_by_pipe_line(cls, pipe_line):
        cls.objects.filter(pipe_line=pipe_line).delete()

    @classmethod
    def get_list_by_pipe_line(cls, pipe_line):
        return list(cls.objects.filter(pipe_line=pipe_line).order_by('order'))

    @classmethod
    def get_current_card_count_by_pipe_line(cls, pipe_line):
        return cls.objects.filter(pipe_line=pipe_line).count()
