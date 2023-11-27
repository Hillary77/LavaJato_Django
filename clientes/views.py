import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente, Carro
import json


def cadastrar(request):
    if request.method == "GET":
        return render(request, 'pages/user/user.create.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        # Enviar dados para a API
        api_url = 'http://127.0.0.1:8000/api/clientes/'
        api_data = {
            'user': user,
            'email': email,
            'nome': nome,
            'sobrenome': sobrenome,
            'endereco': endereco,
            'cidade': cidade,
            'cpf': cpf,
            'cep': cep,
            'carro': carro,
            'placa': placa,
            'ano': ano
        }

        # Configurar cabeçalhos e enviar dados no formato JSON
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            api_url, data=json.dumps(api_data), headers=headers)

        if response.status_code == 201:  # Supondo que a API retorna 201 para a criação bem-sucedida
            return redirect("listar")
        else:
            return HttpResponse(f'Erro ao enviar dados para a API. Código de status: {response.status_code}')


def listar(APIView):
    def get(self, request):
        users = Cliente.objects.all()
        return render(request, 'pages/user/user.index.html', {'users': users})


def edit(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    users = Cliente.objects.all()
    carros = Carro.objects.filter(cliente=id)

    if request.method == "POST":
        # Obtenha os dados do POST
        user = request.POST.get('user')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')

        # Atualize os dados do cliente
        cliente.user = user
        cliente.email = email
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.endereco = endereco
        cliente.cidade = cidade
        cliente.cpf = cpf
        cliente.cep = cep

        cliente.save()

        # Atualize os dados dos carros
        for carro in carros:
            carro.carro = request.POST.getlist('carro')
            carro.placa = request.POST.getlist('placa')
            carro.ano = request.POST.get('ano')
            carro.save()

        # Substitua 'listar' pelo nome da URL para listar os clientes
        return redirect('listar')

    return render(request, 'pages/user/user.edit.html', {'cliente': cliente, 'users': users, 'carros': carros})


def delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    carro = get_object_or_404(Carro, cliente_id=id)
    carro.delete()
    cliente.delete()
    # Substitua 'listar' pelo nome da URL para listar os clientes
    return redirect('listar')
