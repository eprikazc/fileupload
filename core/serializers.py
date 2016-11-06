from rest_framework import serializers

from core.models import FileRecord


class CreateFileRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileRecord
        fields = ('id', 'username', 'uploaded_file')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res.pop('uploaded_file')
        return res


class FileRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileRecord
        fields = ('id', 'username', 'filename')
