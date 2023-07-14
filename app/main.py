

from fastapi import FastAPI

# -- define the app
my_api = FastAPI()


# -- endpoint: get on /
@my_api.get("/")
async def info():
    return {"message": "Welcome to my_api",
            "version": "0.0.900"}


# -- endpoint: get on /item
@my_api.get("/item")
async def item():
    return {"item_id": "0001",
            "item_name": "name",
            "item_number": "2"}
