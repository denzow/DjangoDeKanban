from django.contrib import admin

from .models import Board, Card, PipeLine

admin.site.register(Board)
admin.site.register(Card)
admin.site.register(PipeLine)

