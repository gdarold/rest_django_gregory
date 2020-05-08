from rest_framework.viewsets import ModelViewSet

from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer

