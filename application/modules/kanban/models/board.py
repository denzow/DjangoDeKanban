from django.conf import settings
from django.db import models


class Board(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.owner)

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def is_exist(cls, board_id):
        return Board.objects.filter(id=board_id).exists()

    @classmethod
    def get_by_id(cls, board_id):
        try:
            return cls.objects.get(pk=board_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_list_by_owner(cls, owner):
        return list(cls.objects.filter(owner=owner).order_by('updated_at'))
