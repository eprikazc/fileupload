from rest_framework import serializers

from core.models import FileRecord


class CreateFileRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileRecord
        fields = ('id', 'username', 'uploaded_file')


class FileRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileRecord
        fields = ('id', 'username', 'filename')
