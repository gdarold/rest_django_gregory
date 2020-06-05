from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_fields = ('nome', 'descricao')
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

