from rest_framework import mixins, viewsets

from core.models import FileRecord
from core.serializers import FileRecordSerializer


class FileRecordViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = FileRecord.objects.all()
    serializer_class = FileRecordSerializer
