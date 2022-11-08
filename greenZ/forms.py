from django import forms
from .models import Cidade, Banco, CreditoRural, TipoLicenca, LicencaAmbiental

class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        fields = ('nome_cidade',)

        widgets = {
            'nome_cidade': forms.TextInput(attrs={'class': 'form-control'}),            
        }

class BancoForm(forms.ModelForm):

    class Meta:
        model = Banco
        fields = ('nome_banco',)

        widgets = {
            'nome_banco': forms.TextInput(attrs={'class': 'form-control'}),            
        }

class TipoLicencaForm(forms.ModelForm):

    class Meta:
        model = TipoLicenca
        fields = ('nome_licenca', 'descricao',)

        widgets = {
            'nome_licenca': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),            
        }

class CreditoRuralForm(forms.ModelForm):

    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})),
    banco = forms.ModelChoiceField(queryset=Banco.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})),

    class Meta:
        model = CreditoRural
        fields = ('nome','cpf','rg','telefone','ano_cadastro','valor','juros',
            'situacao','data_pagamento','numero_projeto','analise_previa','atividade',
            'emissao_cedula','seguro','linha_credito','cidade','banco','arquivos',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mCPF );'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mTel );'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_cadastro': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'juros': forms.NumberInput(attrs={'class': 'form-control'}),
            'situacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'data_pagamento': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'numero_projeto': forms.TextInput(attrs={'class': 'form-check-input'}),
            'analise_previa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'atividade': forms.TextInput(attrs={'class': 'form-control'}),
            'emissao_cedula': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'seguro': forms.NumberInput(attrs={'class': 'form-control'}),
            'linha_credito': forms.NumberInput(attrs={'class': 'form-control'}),
            'arquivos': forms.FileInput(attrs={'class': 'form-control'}),
        }

"""class CreditoRuralForm(forms.Form):
    nome = forms.CharField(label='Nome Cliente', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF',max_length=14,widget=forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mCPF );' }))
    rg = forms.CharField(label='RG',max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label='Telefone',max_length=14, widget=forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mTel );'}))
    ano_cadastro = forms.DateTimeField(label='Ano do cadastro', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    valor = forms.DecimalField(label='Valor', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    juros = forms.DecimalField(label='Juros', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    situacao = forms.BooleanField(label='Situação', widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    data_pagamento = forms.DateTimeField(label='Data do pagamento', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    numero_projeto = forms.IntegerField(label='N° do projeto', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    analise_previa = forms.BooleanField(label='Análise prévia', widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    atividade = forms.CharField(label='Atividade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emissao_cedula = forms.DateTimeField(label='Emissão da cédula', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    seguro = forms.DecimalField(label='Seguro', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    linha_credito = forms.DecimalField(label='Linha de crédito', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    banco = forms.ModelChoiceField(queryset=Banco.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    arquivos = forms.FileField(label='Arquivos',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
"""


class LicencaAmbientalForm(forms.ModelForm):
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})),
    tipo_licenca = forms.ModelChoiceField(queryset=TipoLicenca.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})),


    class Meta:
        model = LicencaAmbiental
        fields = ('nome','cpf','rg','telefone','ano_cadastro','data_inicio','data_vencimento',
            'situacao','numero_projeto','cnpj','cidade','tipo_licenca','arquivos',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mCPF );'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mTel );'}),
            'ano_cadastro': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'data_inicio': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'data_vencimento': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}),
            'situacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'numero_projeto': forms.TextInput(attrs={'class': 'form-check-input'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivos': forms.FileInput(attrs={'class': 'form-control'}),
        }


"""
class LicencaAmbientalForm(forms.Form):
    nome = forms.CharField(label='Nome Cliente', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF',max_length=14,widget=forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mCPF );' }))
    rg = forms.CharField(label='RG',max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label='Telefone',max_length=14, widget=forms.TextInput(attrs={'class': 'form-control', 'onkeydown': 'javascript: fMasc( this, mTel );'}))
    ano_cadastro = forms.DateTimeField(label='Ano do cadastro', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    data_inicio = forms.DateTimeField(label='Data do inicio da licença', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    data_vencimento = forms.DateTimeField(label='Data do vencimento', widget=forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class': 'form-control'}))
    situacao = forms.BooleanField(label='Situação', widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    numero_projeto = forms.IntegerField(label='N° do projeto', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    cnpj = forms.CharField(label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_licenca = forms.ModelChoiceField(queryset=TipoLicenca.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    arquivos = forms.FileField(label='Arquivos',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

"""