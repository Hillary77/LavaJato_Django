from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Carro

def cadastrar(request):
   
    if request.method == "GET": 
       return render (request, 'pages/user/user.create.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        carro = request.POST.get('carro')
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')

      
        cliente = Cliente(user=user, email=email, nome=nome, sobrenome=sobrenome, endereco=endereco, cidade=cidade, cpf=cpf, cep=cep)
        cliente.save()

        for carro, placa, ano  in zip(carro,placa,ano):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()
        return redirect("listar")
    
def listar(request):
        users = Cliente.objects.all()
        return render(request, 'pages/user/user.index.html', {'users' : users})

def edit(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    carro = get_object_or_404(Carro, pk=id)
    users = Cliente.objects.all()


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
        carro = request.POST.getlist['carro']
        placa = request.POST.getlist['placa']
        ano = request.POST.getlist['ano']

      

        return redirect('listar')  # Substitua 'user.index' pelo nome da URL para listar os clientes

    return render(request, 'pages/user/user.edit.html',  {'cliente': cliente, 'users': users, 'carro' : carro})