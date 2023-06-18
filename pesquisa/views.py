from django.shortcuts import render
from django.contrib import messages
from urllib.request import Request
from django.http import HttpResponseNotAllowed
from .models import Pesquisa
from .forms import Form_Pesquisa
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'cp/home.html') 

@login_required
def novo_pesquisa(request):
    if request.method == 'POST':
        pesquisa = Form_Pesquisa(request.POST)
        
        if pesquisa.is_valid() :
            pesquisa.atitude_positiva = request.POST['atitude_positiva']
            pesquisa.trabalho_em_equipe = request.POST['trabalho_em_equipe']
            pesquisa.atendimento_eficaz_cliente = request.POST['atendimento_eficaz_cliente']
            pesquisa.comunicação_com_liderança = request.POST['comunicação_com_liderança']
            pesquisa.promoção_união = request.POST['promoção_união']
            pesquisa.melhorar_qualidade = request.POST['melhorar_qualidade']
            pesquisa.criatividade_redução_custos = request.POST['criatividade_redução_custos']
            pesquisa.atitude_diante_mudanças = request.POST['atitude_diante_mudanças']
            pesquisa.ideias_para_bom_ambiente = request.POST['ideias_para_bom_ambiente']
            
            pesquisa.save()
            pesquisa = Form_Pesquisa()

            messages.info(request, 'Inserido com sucesso')
            return redirect('/novo_pesquisa')
 
    else:
        pesquisa = Form_Pesquisa()
    
    return render(request, 'cp/novo_pesquisa.html', {'pesquisa': pesquisa})

@login_required
def consultas(request):
    nome_filtro = request.GET.get('nome')
    dpto_filtro = request.GET.get('dpto') 
    função_filtro = request.GET.get('função')    
    
    if nome_filtro:
        pesquisa = Pesquisa.objects.filter(colaborador__icontains=nome_filtro)
        
    elif dpto_filtro:
        pesquisa = Pesquisa.objects.filter(departamento__icontains=dpto_filtro)  
          
    elif função_filtro:
        pesquisa = Pesquisa.objects.filter(função__icontains=função_filtro)  
    
    else:
        pesquisa = Pesquisa.objects.order_by('colaborador').all()
    
    return render(request, 'cp/consultas.html', {'pesquisa': pesquisa})

@login_required
def editar_lista(request, id):
    editar = get_object_or_404(Pesquisa, pk=id)
    form = Form_Pesquisa(instance=editar)
 
    if request.method == 'POST':
        form = Form_Pesquisa(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
           
            return redirect('/consultas')
   
        else:
            return render(request, 'cp/editar_lista.html', {'form':form ,'editar': editar})  


    return render(request, 'cp/editar_lista.html', {'form':form ,'editar': editar})  

@login_required
def deletar_entrevista(request, id):
    deletar = get_object_or_404(Pesquisa, pk=id)
   
    if request.method == 'POST':
        deletar.delete()

       
        return redirect('/consultas')

    return render(request, 'cp/deletar_entrevista.html')    