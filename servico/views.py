from django.shortcuts import render, redirect,  get_object_or_404
from .models import Servico, CategoriaManutencao, Cliente
from datetime import datetime

def create_servico(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        categorias_create = CategoriaManutencao.objects.all()
        return render(request, 'pages/servico/create_servico.html', {'clientes': clientes, 'categorias_create': categorias_create})
    
    elif request.method == "POST":
        data_init = request.POST.get('data_init')
        data_end = request.POST.get('data_end')
        cliente_id = request.POST.get('cliente_id')
        categorias = request.POST.getlist('id_categoriasmanutencao')
        titulo = request.POST.get('titulo')

        # Transforma os IDs das categorias de manutencao em objetos CategoriaManutencao
        categorias_manutencao = CategoriaManutencao.objects.filter(id__in=categorias)

        servico = Servico(
            data_init=data_init,
            data_end=data_end,
            cliente_id=cliente_id,
            titulo=titulo,
        )
        servico.save()

        # Adiciona as categorias selecionadas ao serviço
        servico.categorias_manutencao.add(*categorias_manutencao)
        return redirect("index_servico")
    # Recupera novamente os clientes e categorias para reexibir o formulário
    clientes = Cliente.objects.all()
    categorias_create = CategoriaManutencao.objects.all()

    return render(request, 'pages/servico/create_servico.html', {'clientes': clientes, 'categorias_create': categorias_create})
    

def index_servico(request):
    clientes = Cliente.objects.all()
    servico = Servico.objects.all()


    return render(request, 'pages/servico/index_servico.html', {'clientes': clientes, 'servico' : servico})

def edit_servico(request, id):
    servicos = get_object_or_404(Servico, pk=id)

    return render(request, 'pages/servico/edit_servico.html', {'servicos': servicos})

def delete_servico(request):
    pass