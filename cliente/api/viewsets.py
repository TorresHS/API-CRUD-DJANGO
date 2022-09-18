from webbrowser import get
from rest_framework import viewsets
from cliente.models import Cliente, Banco
from cliente.api.serializers import ClienteSerializers, BancoSerializers, ClienteDetalhesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class ClienteViewsets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def detalhes(self, resquest, pk=None, *args, **kwargs):
        queryset = Cliente.objects.filter(pk=pk)
        self.serializer_class = ClienteDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

class BancoViewsets(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializers

    permission_classes = [IsAuthenticated]
