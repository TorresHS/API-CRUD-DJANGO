from rest_framework import viewsets
from cliente.models import Cliente, Banco
from cliente.api.serializers import ClienteSerializers, BancoSerializers, ClienteDetalhesSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ClienteViewsets(viewsets.ModelViewSet):
   queryset = Cliente.objects.all()
   serializer_class = ClienteSerializers
   parser_classes = (MultiPartParser,)
   permission_classes = [IsAuthenticated]

   @swagger_auto_schema(
       operation_description='Upload container excel, if the columns and data are valid. Containers will be created. '
                             'If container with such name already exists, it will be update instead',
       operation_id='Upload container excel',
       manual_parameters=[openapi.Parameter(
                           name="file",
                           in_=openapi.IN_FORM,
                           type=openapi.TYPE_FILE,
                           required=True,
                           description="Document"
                           )],
       responses={400: 'Invalid data in uploaded file',
                  200: 'Success'},
   )
   @action(detail=False, methods=['post'])
   def post(self, request, *args, **kwargs): return super(ClienteSerializers, self).post(self, *args, **kwargs)

   @action(detail=True, methods=['get'])
   def detalhes(self, resquest, pk=None, *args, **kwargs):
       queryset = Cliente.objects.filter(pk=pk)
       self.serializer_class = ClienteDetalhesSerializer
       serializer = self.get_serializer(queryset, many=True)

       return Response(serializer.data)

class BancoViewsets(viewsets.ModelViewSet):
   queryset = Banco.objects.all()
   serializer_class = BancoSerializers
   parser_classes = (MultiPartParser,)
   permission_classes = [IsAuthenticated]