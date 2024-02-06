from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers import FileSerializer
from .models import File


class FileView(CreateModelMixin, ListModelMixin, GenericViewSet):
    """Добавление Position в БД."""
    serializer_class = FileSerializer
    queryset = File.objects.all()
