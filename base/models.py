from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    data_alteracao = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    ativo = models.BooleanField(default=False, null=True, blank=True)
    contato = models.ForeignKey(Contato, null=True, blank=True, on_delete=models.SET_NULL)
    data_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.titulo



