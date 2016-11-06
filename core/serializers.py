from rest_framework import serializers

from core.models import FileRecord


# class FileRecordSerializer(serializers.ModelSerializer):
class FileRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FileRecord
        fields = ('id', 'username', 'uploaded_file', 'filename', 'archive_name')

    filename = serializers.SerializerMethodField()
    archive_name = serializers.SerializerMethodField()

    def get_filename(self, obj):
        return obj.uploaded_file.name

    def get_archive_name(self, obj):
        return obj.zipped_file.name
