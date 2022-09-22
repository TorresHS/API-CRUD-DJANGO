from django.db import models
import requests

import requests

def get_banco_names_with_code() -> tuple:
   banks = requests.get('https://brasilapi.com.br/api/banks/v1').json()
   return [ (bank['ispb'], bank['fullName']) for bank in banks ]

# P/ CHOICES
# (
#     []
# )


       # An example of a custom manager called "objects".
class BancoManager(models.Manager):
   def get_name_bank_and_count_list_by_id(self,banco_id:str):
       banks = self.filter(banco=banco_id)
       qtd_rep = len(banks)

       bank_name = self.get_name_bank(banco_id)

       return (bank_name, qtd_rep)


   def get_name_bank(self,id):
       res = requests.get("https://brasilapi.com.br/api/banks/v1").json()
       for bank in res:
           if bank['ispb'] == id:
               return bank['fullName']

# Create your models here.
class Cliente(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=255)
   email = models.EmailField(unique=True)
   telefone = models.BigIntegerField(unique=True)
   endereco = models.CharField(max_length=255)
   data_de_cadastro = models.DateField(null=True,blank=False)
   faturamento_declarado = models.FileField(upload_to='faturamentos/',null=True,blank=False)

   def __str__(self) -> str:
       return self.nome

   class Meta:
       db_table = 'cliente'
       managed = True


class Banco(models.Model):
   id = models.AutoField(primary_key=True)
   agencia = models.CharField(max_length=20,blank=False,null=False)
   conta = models.BigIntegerField()
   banco = models.CharField(max_length=255,choices=get_banco_names_with_code())
   cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='banco')
   objects = BancoManager()

   class Meta:
       db_table = 'banco'
       unique_together = ('conta','banco')

