import os

from tempfile import NamedTemporaryFile
from zipfile import ZipFile

from background_task import background
from core.models import FileRecord
from django.core.files import File


@background(schedule=1)
def zip_upload(file_record_id):
    """
    Takes id of file record in db, reads uploaded file and ZIPs it
    """
    obj = FileRecord.objects.get(id=file_record_id)
    source_file_name = os.path.basename(obj.uploaded_file.path)
    zipped_upload_file_name = _prepare_zip_file(obj.uploaded_file.path)
    with zipped_upload_file_name:
        obj.zipped_file.save(
            source_file_name + '.zip',
            File(zipped_upload_file_name))
    obj.save()


def _prepare_zip_file(source_file_name):
    target_file_name = NamedTemporaryFile()
    with ZipFile(target_file_name, 'w') as my_zipfile:
        my_zipfile.write(
            source_file_name,
            os.path.basename(source_file_name))
    return target_file_name
