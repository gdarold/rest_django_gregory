from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario


class ComentarioViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
