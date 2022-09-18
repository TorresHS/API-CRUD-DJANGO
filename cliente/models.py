from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.BigIntegerField(unique=True)
    endereco = models.CharField(max_length=255)
    data_de_cadastro = models.DateField()
    faturamento_declarado = models.FileField(upload_to='faturamentos/')

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = 'cliente'


class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    agencia = models.BigIntegerField()
    conta = models.BigIntegerField(unique=True)
    banco = models.CharField(max_length=255)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='banco')

    class Meta:
        db_table = 'banco'