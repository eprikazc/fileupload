from django.db import models


class FileRecord(models.Model):
    username = models.CharField(max_length=30)
    uploaded_file = models.FileField()
