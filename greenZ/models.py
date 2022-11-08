from django.db import models

class Cidade(models.Model):
	nome_cidade = models.CharField(max_length= 100)

	def __str__(self) -> str:
		return self.nome_cidade

class Banco(models.Model):
	nome_banco = models.CharField(max_length= 50)

	def __str__(self) -> str:
		return self.nome_banco

class CreditoRural(models.Model):
	nome = models.CharField(max_length= 100)
	cpf = models.CharField(max_length= 18)
	rg = models.CharField(max_length = 15)
	telefone = models.CharField(max_length = 13)
	ano_cadastro = models.DateField()
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	juros = models.DecimalField(max_digits=10, decimal_places=2)
	situacao = models.BooleanField()
	data_pagamento = models.DateField()
	numero_projeto = models.CharField(max_length= 25)
	analise_previa = models.BooleanField()
	atividade = models.CharField(max_length= 100)
	emissao_cedula = models.DateField()
	seguro = models.DecimalField(max_digits=10, decimal_places=2)
	linha_credito = models.DecimalField(max_digits=10, decimal_places=2)
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
	banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
	arquivos = models.FileField(upload_to='Files/CreditoRural')

class TipoLicenca(models.Model):
	nome_licenca = models.CharField(max_length= 50)
	descricao = models.CharField(max_length= 500)

	def __str__(self) -> str:
		return self.nome_licenca

class LicencaAmbiental(models.Model):
	nome = models.CharField(max_length= 100)
	cpf = models.CharField(max_length= 18)
	rg = models.CharField(max_length= 15)
	telefone = models.CharField(max_length=13)
	ano_cadastro = models.DateField()
	data_inicio = models.DateField()
	data_vencimento = models.DateField()
	situacao = models.BooleanField()
	numero_projeto = models.CharField(max_length= 25)
	cnpj = models.CharField(max_length= 25)
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
	tipo_licenca = models.ForeignKey(TipoLicenca, on_delete=models.CASCADE)
	arquivos = models.FileField(upload_to='Files/LicencaAmbiental')



