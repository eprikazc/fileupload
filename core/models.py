import os

from tempfile import NamedTemporaryFile
from zipfile import ZipFile

from django.core.files import File
from django.db import models


class FileRecord(models.Model):
    username = models.CharField(max_length=30)
    # When uploading files with the same name Django will add unique suffix
    # We use "filename" field to store original (not modified) file name
    filename = models.CharField(max_length=100)
    uploaded_file = models.FileField('uploads/', max_length=100)
    zipped_file = models.FileField('zipped/', blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.username, self.uploaded_file.name)

    def zip_upload(self):
        source_file_name = os.path.basename(self.uploaded_file.path)
        zipped_upload_file_name = prepare_zip_file(self.uploaded_file.path)
        with zipped_upload_file_name:
            self.zipped_file.save(
                source_file_name + '.zip',
                File(zipped_upload_file_name))


def prepare_zip_file(source_file_name):
    target_file_name = NamedTemporaryFile()
    with ZipFile(target_file_name, 'w') as my_zipfile:
        my_zipfile.write(
            source_file_name,
            os.path.basename(source_file_name))
    return target_file_name
