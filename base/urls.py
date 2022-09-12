from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('tarefas/', views.tarefaList, name='tarefaList'),
    path('detalhe-tarefa/<str:pk>/', views.tarefaDetalhe, name='tarefaDetalhe'),
    path('criar-tarefa/', views.createTarefa, name='createTarefa'),
    path('atualizar-tarefa/<str:pk>/', views.atualizarTarefa, name='atualizarTarefa'),
    path('deletar-tarefa/<str:pk>', views.excluirTarefa, name='excluirTarefa'),

    path('contatos/', views.contatoList, name='contatoList'),
    path('detalhe-contato/<str:pk>', views.contatoDetalhe, name='contatoDetalhe'),
    path('criar-contato/', views.createContato, name='createContato'),
    path('atualizar-contato/<str:pk>', views.atualizarContato, name='atualizarContato'),
    path('deletar-contato/<str:pk>', views.excluirContato, name='excluirContato'),
]