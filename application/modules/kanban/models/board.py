from django.conf import settings
from django.db import models


class Board(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.owner)
