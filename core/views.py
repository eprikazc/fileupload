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
        instance.save()

    @decorators.detail_route(methods=['get'])
    def zipped(self, request, pk):
        obj = self.get_object()
        return self._serve(obj.zipped_file.path, obj.filename + '.zip')

    @decorators.detail_route(methods=['get'])
    def unzipped(self, request, pk):
        obj = self.get_object()
        return self._serve(obj.uploaded_file.path, obj.filename)

    def _serve(self, full_path, file_name):
        # Based on django.views.static.static
        statobj = os.stat(full_path)
        content_type, encoding = mimetypes.guess_type(full_path)
        content_type = content_type or 'application/octet-stream'
        response = FileResponse(open(full_path, 'rb'), content_type=content_type)
        response['Last-Modified'] = http_date(statobj.st_mtime)
        if stat.S_ISREG(statobj.st_mode):
            response['Content-Length'] = statobj.st_size
        if encoding:
            response['Content-Encoding'] = encoding
        response['Content-Disposition'] = 'inline; filename="%s"' % file_name
        return response
