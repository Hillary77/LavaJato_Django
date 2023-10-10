import requests
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Servico, CategoriaManutencao, Cliente
from django.http import HttpResponse, FileResponse
from datetime import datetime
#Gerar pdf de nota fiscal
from fpdf import FPDF 
import json
from io import BytesIO

def create_servico(request):
    if request.method == "GET":
        # Recupera todos os clientes e categorias para exibir no formulário
        clientes = Cliente.objects.all()
        categorias_create = CategoriaManutencao.objects.all()
        return render(request, 'pages/servico/create_servico.html', {'clientes': clientes, 'categorias_create': categorias_create})
    
    elif request.method == "POST":
        data_init = request.POST.get('data_init')
        data_end = request.POST.get('data_end')
        cliente_id = request.POST.get('cliente_id')
        categorias = request.POST.getlist('id_categoriasmanutencao')
        titulo = request.POST.get('titulo')

        categorias_manutencao = CategoriaManutencao.objects.filter(id__in=categorias)

      
        # URL da API
        api_url = 'http://127.0.0.1:8000/api/servico/'  
        # Substitua pela URL correta

        # Dados a serem enviados para a API
        api_data = {
            'data_init': data_init,
            'data_end': data_end,
            'cliente_id': cliente_id,
            'categorias': categorias,
            'titulo': titulo
        }

        # Configuração dos cabeçalhos
        headers = {'Content-Type': 'application/json'}

        # Envia os dados para a API usando o método POST
        response = requests.post(api_url, data=json.dumps(api_data), headers=headers)

        # Verifica se a resposta da API indica uma criação bem-sucedida (código de status 201)
        if response.status_code == 201:
            return redirect("index_servico")
        else:
            return HttpResponse(f'Erro ao enviar dados para a API. Código de status: {response.status_code}')

    # Se o método não for GET nem POST, recupera novamente os clientes e categorias para reexibir o formulário
    clientes = Cliente.objects.all()
    categorias_create = CategoriaManutencao.objects.all()
    return render(request, 'pages/servico/create_servico.html', {'clientes': clientes, 'categorias_create': categorias_create})

def index_servico(request):
    clientes = Cliente.objects.all()
    servico = Servico.objects.all()


    return render(request, 'pages/servico/index_servico.html', {'clientes': clientes, 'servico' : servico})

def edit_servico(request, id):
    
    servico = get_object_or_404(Servico, pk=id)
    clientes = Cliente.objects.all()
    categorias = CategoriaManutencao.objects.all()

    if request.method == "POST":
        # Obtenha os dados do POST
        titulo = request.POST.get('titulo')
        cliente_id = request.POST.get('cliente_id')
        categorias_selecionadas = request.POST.getlist('id_categoriasmanutencao')
        data_init = request.POST.get('data_init')
        data_end = request.POST.get('data_end')

        servico.titulo = titulo
        servico.cliente = Cliente.objects.get(pk=cliente_id)
        servico.categorias_manutencao.set(categorias_selecionadas)
        servico.data_init = data_init
        servico.data_end = data_end
        servico.save()

        return redirect('index_servico')  # Redirecione para a página index após a edição

    return render(request, 'pages/servico/edit_servico.html', {'servico': servico, 'clientes': clientes, 'categorias': categorias})

def delete_servico(request, id):
    servico = get_object_or_404(Servico, pk=id)
    servico.delete()
    return redirect('index_servico')  # Redirecione para a página apropriada após a edição


def gerar_pdf(request,id):
    servicos = Servico.objects.all()
    servico = get_object_or_404(Servico, pk=id)
    print(servico.valor_total)
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'I', 16)
    pdf.cell(190,15,'Nota de serviços', 0, 1, 'L', 0)

    pdf.set_font('Arial', 'B', 12)

    pdf.cell(35,10,'Cliente:', 1, 0, 'L', 0)
    pdf.cell(0,10,f'{servico.cliente.nome}', 1, 1, 'L', 0)

    pdf.cell(35,10,'Título:', 1, 0, 'L', 0)
    pdf.cell(0,10,f'{servico.titulo}', 1, 1, 'L', 0)

    pdf.cell(35,10,'Manutenções:', 1, 0, 'L', 0)

    categorias_manutencao = servico.categorias_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):
        pdf.cell(0, 10, f'+ {manutencao.get_titulo_display()}', 1, 1, 'L', 0)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(35, 10, 'Data de Início:', 1, 0, 'L', 0)
    pdf.cell(0, 10, f'{servico.data_init}', 1, 1, 'L', 0)

    pdf.cell(35, 10, 'Data de Fim:', 1, 0, 'L', 0)
    pdf.cell(0, 10, f'{servico.data_end}', 1, 1, 'L', 0)

    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 0)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 0)

    pdf.set_font('Arial', 'I', 12)
    pdf.cell(20,10,'Preço servicos:', 0, 1, 'L', 0)

    
    pdf.cell(170,10,f'{servico.valor_total}', 0, 1, 'L', 0)
 
 
    #pdf.cell(170,10,(date('H:i:m d-m-Y ')), 0, 1, 'L', 0)
    
    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)
   
    return FileResponse(pdf_bytes, filename=f"{servico.protocolo}.pdf")



