import os

from django.core.files import File
from django.db import models


class FileRecord(models.Model):
    username = models.CharField(max_length=30)
    uploaded_file = models.FileField(
        upload_to='uploads/', max_length=100, help_text="File")
    zipped_file = models.FileField(
        upload_to='zipped/', blank=True, null=True, help_text="Archived File")
    # We need to store original file name, because
    # Django adds unique suffix when uploading files with the same name
    # This filename is used to serve files via API
    filename = models.CharField(max_length=100, help_text="Original filename")

    def __str__(self):
        return '%s: %s' % (self.username, self.uploaded_file.name)
