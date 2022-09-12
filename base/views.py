from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa, Contato

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TarefaSerializer, ContatoSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(req):
    basePoint = 'PONTO DE BASE DA API';
    api_urls = [
       [ 
      {'Listar': '/tarefas'},
      {'Detalhe Tarefa': '/detalhe-tarefa/<str:pk>'},
      {'Criar': '/criar-tarefa/'},
      {'Atualizar': '/atualizar-tarefa/<str:pk>'},
      {'Excluir': '/deletar-tarefa/<str:pk>'},
       ],
       [
      {'Listar': '/contatos'},
      {'Detalhe Contato': '/detalhe-contato/<str:pk>'},
      {'Criar': '/criar-contato/'},
      {'Atualizar': '/atualizar-contato/<str:pk>'},
      {'Excluir': '/deletar-contato/<str:pk>'},
      ],
    ]
    return Response(api_urls);


@api_view(['GET'])
def tarefaList(req):
    tarefas = Tarefa.objects.all();
    serializer = TarefaSerializer(tarefas, many=True);
    return Response(serializer.data);


@api_view(['GET'])
def tarefaDetalhe(req, pk):
    tarefa = Tarefa.objects.get(id=pk);
    serializer = TarefaSerializer(tarefa, many=False);
    return Response(serializer.data);

@api_view(['POST'])
def createTarefa(request):
    serializer = TarefaSerializer(data=request.data);
    print(serializer)

    # print("is valid?????")
    print(serializer.is_valid);
    if serializer.is_valid():
        print("is valid!!")
        serializer.save();

    return Response(serializer.data)


@api_view(['POST'])
def atualizarTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk); 
    serializer = TarefaSerializer(instance=tarefa, data=request.data);

    if serializer.is_valid():
        serializer.save();

    return Response(serializer.data)


@api_view(['DELETE'])
def excluirTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk); 
    tarefa.delete();

    return Response('Tarefa deletada com sucesso')


@api_view(['GET'])
def contatoList(req):
    contato = Contato.objects.all();
    serializer = ContatoSerializer(contato, many=True);
    return Response(serializer.data);

@api_view(['GET'])
def contatoDetalhe(req, pk):
    contato = Contato.objects.get(id=pk);
    serializer = ContatoSerializer(contato, many=False);
    return Response(serializer.data);


@api_view(['POST'])
def createContato(request):
    serializer = ContatoSerializer(data=request.data);

    if serializer.is_valid():
        serializer.save();

    return Response(serializer.data)


@api_view(['POST'])
def atualizarContato(request, pk):
    contato = Contato.objects.get(id=pk); 
    serializer = ContatoSerializer(instance=contato, data=request.data);

    if serializer.is_valid():
        serializer.save();

    return Response(serializer.data)


@api_view(['DELETE'])
def excluirContato(request, pk):
    contato = Contato.objects.get(id=pk); 
    contato.delete();

    return Response('Contato deletado com sucesso')