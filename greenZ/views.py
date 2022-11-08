from django.shortcuts import render, redirect
from .forms import CidadeForm, BancoForm, TipoLicencaForm, CreditoRuralForm, LicencaAmbientalForm
from .models import Cidade, Banco, CreditoRural, TipoLicenca, LicencaAmbiental


def index(request):
    return render(request, 'greenZ/index.html', {})

def add_cidade(request):
    if request.method == "POST":
        form = CidadeForm(request.POST)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.save()           
            return redirect('/add_cidade')
    else:
        form = CidadeForm()
    return render(request, 'greenZ/add_city.html', {'form': form})

def cidade_list(request):
    cidade_list = Cidade.objects.all()
    return render(request, 'greenZ/list_city.html', {'cidade_list': cidade_list})

def add_banco(request):
    if request.method == "POST":
        form = BancoForm(request.POST)
        if form.is_valid():
            banco = form.save(commit=False)
            banco.save()           
            return redirect('/add_banco')
    else:
        form = BancoForm()
    return render(request, 'greenZ/add_bank.html', {'form': form})

def banco_list(request):
    banco_list = Banco.objects.all()
    return render(request, 'greenZ/list_bank.html', {'banco_list': banco_list})

def add_tipoLicenca(request):
    if request.method == "POST":
        form = TipoLicencaForm(request.POST)
        if form.is_valid():
            tp = form.save(commit=False)
            tp.save()           
            return redirect('/add_tipoLicenca')
    else:
        form = TipoLicencaForm()
    return render(request, 'greenZ/add_typeLicenca.html', {'form': form})

def tipoLicenca_list(request):
    tipoLicenca_list = TipoLicenca.objects.all()
    return render(request, 'greenZ/list_tipolicenca.html', {'tipoLicenca_list': tipoLicenca_list})

def add_creditoRural(request):
    if request.method == "POST":
        form = CreditoRuralForm(request.POST)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.save()           
            return redirect('/add_creditoRural')
    else:
        form = CreditoRuralForm()
    return render(request, 'greenZ/add_cr.html', {'form': form})

def credito_list(request):
    credito_list = CreditoRural.objects.all()
    return render(request, 'greenZ/list_credito.html', {'credito_list': credito_list})

def add_licencaAmbiental(request):
    if request.method == "POST":
        form = LicencaAmbientalForm(request.POST)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.save()           
            return redirect('/add_licencaAmbiental')
    else:
        form = LicencaAmbientalForm()
    return render(request, 'greenZ/add_la.html', {'form': form})

def licenca_list(request):
    licenca_list = LicencaAmbiental.objects.all()
    return render(request, 'greenZ/list_licenca.html', {'licenca_list': licenca_list})