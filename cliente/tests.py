from django.test import TestCase
from cliente.models import Banco, Cliente
import requests

class AppTest(TestCase):

   def setUp(self):
       #to right data
       self.myClient = Cliente.objects.create(nome='nome',email='g@g.com', telefone=1195785211,endereco="Rua 7",data_de_cadastro=None,faturamento_declarado=None)

       self.myBancs = []
       self.myBancs.append(Banco.objects.create(agencia='0001',conta=8875465468,banco='00360305',cliente=self.myClient))
       self.myBancs.append(Banco.objects.create(agencia='0001',conta=55353,banco='00416968',cliente=self.myClient))
       self.myBancs.append(Banco.objects.create(agencia='0001',conta=5353535353,banco='00416968',cliente=self.myClient))


       #to wrong data
       self.myClient2 = Cliente.objects.create(nome='nome',email='gg@g.com', telefone=11957855211,endereco="Rua 7",data_de_cadastro=None,faturamento_declarado=None)

       self.myBancs2 = []
       self.myBancs2.append(Banco.objects.create(agencia='0001',conta=8875465468,banco='003603055505',cliente=self.myClient))
       self.myBancs2.append(Banco.objects.create(agencia='0001',conta=55353,banco='00416968880',cliente=self.myClient))
       self.myBancs2.append(Banco.objects.create(agencia='0001',conta=5353535353,banco='00416968880',cliente=self.myClient))


   def test_assimilate_bank_name_with_api_at_least_one(self):
       # se var == 0 então não tem, caso contrario, tem.

       res = requests.get('https://brasilapi.com.br/api/banks/v1')
       data = res.json()

       var = 0
       for bank in self.myBancs:
           for bank_api in data:
               if bank_api['ispb'] == bank.banco :

                   var += 1

       self.assertNotEqual(0,var,"Os bancos cadastrados não estão presentes em brasil.api")

   def test_not_assimilate_bank_name_with_api_at_least_one(self):
       res = requests.get('https://brasilapi.com.br/api/banks/v1')
       data = res.json()

       var = 0
       for bank in self.myBancs2:
           for bank_api in data:
               if bank_api['ispb'] == bank.banco :
                   var += 1

       self.assertEqual(0,var,"Os bancos falso positivos estão constando em brasil.api")    


   def test_assimilate_bank_name_with_id(self):
       sample_data = [{
           "ispb": "00806535",
           "name": "PLANNER CV S.A.",
           "code": 100,
           "fullName": "Planner Corretora de Valores S.A."
       },
       {
           "ispb": "00997185",
           "name": "BCO B3 S.A.",
           "code": 96,
           "fullName": "Banco B3 S.A."
       },
       {
           "ispb": "01023570",
           "name": "BCO RABOBANK INTL BRASIL S.A.",
           "code": 747,
           "fullName": "Banco Rabobank International Brasil S.A."
       }]    

       for data in sample_data:
           name_from_sample_data = data['fullName']
           name_from_api = Banco.objects.get_name_bank(data['ispb']) # CUSTOM FUNCTION
           self.assertEqual( name_from_sample_data , name_from_api )

   def test_not_assimilate_bank_name_with_id(self):
       sample_data = [{
           "ispb": "00806535",
           "name": "PLANNER CV S.A.",
           "code": 100,
           "fullName": "BANCU Corretora de Valores S.A."
       },
       {
           "ispb": "00997185",
           "name": "BCO B3 S.A.",
           "code": 96,
           "fullName": "BANCU B3 S.A."
       },
       {
           "ispb": "01023570",
           "name": "BCO RABOBANK INTL BRASIL S.A.",
           "code": 747,
           "fullName": "BANCU Rabobank International Brasil S.A."
       }]    

       for data in sample_data:
           name_from_sample_data = data['fullName']
           name_from_api = Banco.objects.get_name_bank(data['ispb'])
           self.assertNotEqual( name_from_sample_data , name_from_api )

   def test_assimilate_bank_name_and_rep_func(self):
       bank_name, qtd_rep = Banco.objects.get_name_bank_and_count_list_by_id('00416968')
       self.assertEqual(qtd_rep,2)
       self.assertEqual(bank_name,'Banco Inter S.A.')

   def test_not_assimilate_bank_name_and_rep_func(self):
       bank_name, qtd_rep = Banco.objects.get_name_bank_and_count_list_by_id('00416968')
       self.assertNotEqual(qtd_rep,20)