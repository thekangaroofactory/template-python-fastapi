# template-python-fastapi
Template deployment scenario for Python API using FastAPI

## Build Docker container
docker build --tag template-fastapi .

## Run docker image
8000 because dockerfile says CMD ["uvicorn", ... "--port", "8000"]
docker run --name FastAPI -d -p 8000:80 template-fastapi

## Access the API via:
http://localhost:8000/
http://localhost:8000/item
