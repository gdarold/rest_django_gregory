from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

   # def list(self, request, *args, **kwargs):
    #    return Response({'teste':123})

    #def create(self, request, *args, **kwargs):
     #   return Response({'hello':request.data['nome']})

    #def destroy(self, request, *args, **kwargs):
     #   pass

    #def retrieve(self, request, *args, **kwargs):
    #   pass

    #def update(self, request, *args, **kwargs):
     #   pass

    #def partial_update(self, request, *args, **kwargs):
     #   pass

    #aulas 23
   # @action(methods=['post','get'], detail=True)
    #def denunciar(self, request, pk=None):
     #   pass

    #@action(methods=[ 'get'], detail=True)
    #def teste(self, request, pk=None):
     #   pass


