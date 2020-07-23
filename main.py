from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# path parameters
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# path parameters with types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": "item_id"}


# path ordering(most specific first)
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# predefined values
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):  # type annotation
    if model_name == ModelName.alexnet:  # compare enumeration members
        return {"model_name": model_name, "message": "Deep Learing FTW!"}

    if model_name.value == "lenet":  # get the enumeration value
        return {"model": model_name, "message": "LeCNN all the images"}

    return {"model": model_name, "message": "Have some residuals"}


# path parameters containing paths
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
    In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.
    """
    return {"file_path": file_path}
