from django.contrib import admin

# Register your models here.

from .models import Tarefa, Contato

admin.site.register(Tarefa)
admin.site.register(Contato)