import mimetypes
import os
import stat

from django.http import FileResponse
from django.utils.http import http_date
from rest_framework import decorators, mixins, viewsets

from core.models import FileRecord
from core.serializers import CreateFileRecordSerializer, FileRecordSerializer


class FileRecordViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = FileRecord.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateFileRecordSerializer
        return FileRecordSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.filename = serializer.initial_data['uploaded_file'].name
        instance.zip_upload()
