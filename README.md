docker build -t django-backend .
docker run --publish 8000:8000 django-backend
