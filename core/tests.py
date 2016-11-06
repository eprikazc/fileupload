from django.core.files.base import ContentFile
from django.test import TestCase

from core.models import FileRecord
from core.zip_utils import zip_upload


class UploadTestCase(TestCase):
    def setUp(self):
        self.obj = FileRecord(
            username='Bob',
            filename='1.txt',
            uploaded_file=ContentFile('this is content', '1.txt')
        )
        self.obj.save()

    def assertHeader(self, response, header_name, value):
        self.assertEqual(
            response._headers[header_name.lower()],
            (header_name, value))

    def test_listing(self):
        res = self.client.get('/api/uploads/')
        self.assertEqual(
            res.json(),
            [{'username': 'Bob', 'filename': '1.txt', 'id': 1}])

    def test_zipped_error(self):
        res = self.client.get('/api/uploads/1/zipped/')
        self.assertEqual(
            res.json(),
            {'message': 'Archive is not ready yet'})

    def test_zipped_ok(self):
        zip_upload.now(self.obj.id)
        res = self.client.get('/api/uploads/1/zipped/')
        self.assertEqual(res.status_code, 200)
        self.assertHeader(res, 'Content-Type', 'application/zip')
        self.assertHeader(res, 'Content-Disposition', 'inline; filename="1.txt.zip"')

    def test_upload(self):
        with open('example/test_upload.txt') as fp:
            res = self.client.post('/api/uploads/', {'username': 'Ann', 'uploaded_file': fp})
        self.assertEqual(
            res.json(),
            {'id': 2, 'username': 'Ann'}
                )
        res = self.client.get('/api/uploads/')
        self.assertEqual(
            res.json(),
            [
                {'username': 'Bob', 'filename': '1.txt', 'id': 1},
                {'filename': 'test_upload.txt', 'id': 2, 'username': 'Ann'},
            ])
