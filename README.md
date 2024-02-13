# template-python-fastapi

Template for Python API using FastAPI.

## Deployment scenario

- The API is wrapped in a Docker container.
- It uses Uvicorn as ASGI web server.
- The template includes a GitLab CI YAML file to push the Docker image in a container registry.

## GitHub

Repository secrets are needed 

on GitHub side:

- TARGET_URL
- TARGET_USERNAME
- TARGET_TOKEN

on GitLab side:

- define a project TOKEN

## Build Docker container

```
docker build --tag template-fastapi .
```

## Run docker image

Port 8000 because dockerfile says CMD ["uvicorn", ... "--port", "8000"]

```
docker run --name FastAPI -d -p 8000:80 template-fastapi
```

## Access the API via:

- root: http://localhost:8000/ 
- item route: http://localhost:8000/item