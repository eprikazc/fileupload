# File upload service
This is demo file upload app

## Installation

    pip install -r requirements.txt
    python manage.py makemigrations background_task
    python manage.py migrate

## Run development server

    python manage.py runserver

## Run process to execute background tasks

    python manage.py process_tasks

After that you can visit http://localhost:8000/api/ to view self-browseable API

## Unit testing

    python manage.py test core.tests

## Live testing via CURL

List:

    curl -i http://localhost:8000/api/uploads/

Upload:

    curl -i http://localhost:8000/api/uploads/ -F username=Bob -F "uploaded_file=@example/test_upload.txt"

Download:

    curl -i http://localhost:8000/api/uploads/12/zipped/
    # Or
    curl -i http://localhost:8000/api/uploads/12/unzipped/
