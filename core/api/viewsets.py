from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = PontoTuristicoSerializer
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    #permission_classes = [DjangoModelPermissions,]

    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    #lookup_field = 'nome'#altera compotamento padrão de busco # campo tem que ser unico para funcionar

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset.filter(nome__iexact=nome)

        if descricao:
            queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    #aulas 23
   # @action(methods=['post','get'], detail=True)
    #def denunciar(self, request, pk=None):
     #   pass

    #@action(methods=[ 'get'], detail=True)
    #def teste(self, request, pk=None):
     #   pass


