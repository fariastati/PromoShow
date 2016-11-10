from django.db import models

# Create your models here.

class Usuario(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11)
	email = models.EmailField()
	telefone = models.CharField(max_length=12)
	endereco = models.CharField(max_length=100)
	cep = models.CharField(max_length=8)
	estado = models.CharField(max_length=15)
