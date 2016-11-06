# File upload service
This is demo file upload app

## Unit testing

        python manage.py test core.tests

## Test via CURL
First, run development server:

        python manage.py runserver

List:

        curl -i http://localhost:8000/api/uploads/

Upload:

        curl http://localhost:8000/api/uploads/ -F username=Bob -F "uploaded_file=@example/test_upload.txt"

Download:

        curl http://localhost:8000/api/uploads/12/zipped/
        # Or
        curl http://localhost:8000/api/uploads/12/unzipped/

