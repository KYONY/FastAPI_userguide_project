from enum import Enum
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


#
# class ModelName(str, Enum):
# 	alexnet = "alexnet"
# 	resnet = "resnet"
# 	lenet = "lenet"
#
#
# app = FastAPI()

#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get('/')
# async def root():
# 	return {'message': 'Hellow World'}
#
#
# @app.get("/users/me")
# async def read_user_me():
# 	return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
# 	return {"user_id": user_id}
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
# 	if model_name == ModelName.alexnet:
# 		return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
# 	if model_name.value == "lenet":
# 		return {"model_name": model_name, "message": "LeCNN all the images"}
#
# 	return {"model_name": model_name, "message": "Have some residuals"}
#
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
# 	return {"file_path": file_path}
#
#
# @app.get("/fake_items_db/")
# async def read_item(skip: int = 0, limit: int = 10):
# 	return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items_optional/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
# 	if q:
# 		return {"item_id": item_id, "q": q}
# 	return {"item_id": item_id}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
# 	item = {"item_id": item_id}
# 	if q:
# 		item.update({"q": q})
# 	if not short:
# 		item.update(
# 			{"description": "This is an amazing item that has a long description"}
# 		)
# 	return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
# 						user_id: int,
# 						item_id: str,
# 						q: Optional[str] = None,
# 						short: bool = False):
# 	"""http://127.0.0.1:8000/users/234/items/string?q=q%3D1&short=true
# 	http://127.0.0.1:8000/users/234/items/string?q=string&short=false
# 	"""
# 	item = {"item_id": item_id, "owner_id": user_id}
# 	if q:
# 		item.update({"q": q})
# 	if not short:
# 		item.update(
# 			{"description": "This is an amazing item that has a long description"}
# 		)
# 	return item
#
#
# @app.get("/items-required/{item_id}")
# async def read_user_item(item_id: str, needy: str):
# 	"""http://127.0.0.1:8000/items-required/item?needy=needy234"""
# 	item = {"item_id": item_id, "needy": needy}
# 	return item
#
#
# @app.get("/items-required-2/{item_id}")
# async def read_user_item(
# 		item_id: str,
# 		needy: str,
# 		skip: int = 0,
# 		limit: Optional[int] = None):
# 	"""http://127.0.0.1:8000/items-required-2/item23?needy=needly25&skip=1&limit=55"""
# 	item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
# 	return item
#

class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None



app = FastAPI()


@app.post("/items_1/")
async def create_item_1(item: Item):
	item.name = "Vasya"
	return item


@app.post("/items_2/")
async def create_item_2(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price_with_tax": price_with_tax})
	return item_dict



@app.put("/items_3/{item_id}")
async def create_item(item_id: int, item: Item):
	return {"item_id": item_id, **item.dict()}



@app.put("/items_4/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result