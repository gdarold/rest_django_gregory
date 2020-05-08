from rest_framework.viewsets import ModelViewSet

from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

