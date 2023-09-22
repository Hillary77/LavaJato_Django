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
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

      
        cliente = Cliente(user=user, email=email, nome=nome, sobrenome=sobrenome, endereco=endereco, cidade=cidade, cpf=cpf, cep=cep)
        cliente.save()

    for c, p, a in zip(carro, placa, ano):
        car = Carro(carro=c, placa=p, ano=a, cliente=cliente)
        car.save()

        return redirect("listar")
    
def listar(request):
        users = Cliente.objects.all()
        return render(request, 'pages/user/user.index.html', {'users' : users})

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
            carro.carro = request.POST.get('carro')
            carro.placa = request.POST.get('placa')
            carro.ano = request.POST.get('ano')
            carro.save()
    
        return redirect('listar')  # Substitua 'listar' pelo nome da URL para listar os clientes

    return render(request, 'pages/user/user.edit.html', {'cliente': cliente, 'users': users, 'carros': carros})



def delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    carro = get_object_or_404(Carro, cliente_id=id)
    carro.delete()
    cliente.delete()
    return redirect('listar')  # Substitua 'listar' pelo nome da URL para listar os clientes