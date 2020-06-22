from django.db import models
from datetime import datetime

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuario'


class Compras(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    cpf_compra = models.CharField(max_length=11)
    data = models.DateTimeField(verbose_name='Data do Evento')
    valor = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    percent_cashback = models.CharField(max_length=50)
    cashback = models.CharField(max_length=50)

    class Meta:
        db_table = 'compras'

    def get_data_input(self):
        return self.data.strftime('%Y-%m-%dT')
