from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'Detail':{'Name':'Sarang'}}

@app.get('/about')
def about():
    return {'Detail':{'Company': 'Argusoft'}}

@app.get('/show/unpublished')
def show():
    return "These are unpublished blogs."

@app.get('/show/{id}')
def show(id: int):
    return {'Detail':{'ID': id}}

@app.get('/show/{id}/comments')
def show(id: int):
    return {'Detail':{1,2,3,4,5}}

@app.get('/show/{id}/comments')
def content(id: int, limit=10):
    return limit
    
@app.get('/blog')
def index(limit:int=10, published:bool=True, sort:Optional[str]= None):
    if published:
        return f"{limit} published blogs found."
    else:
        return f"{limit} blogs found."


#For passing post parameters in post methods we need to create a class, which will act as a model.
#For making a model we need to import basemodel from pydantic.

class Blog(BaseModel):
    title : str
    body : str
    published : Optional [bool]

@app.post('/blog')
def create_blog(blog : Blog):
    return f"Blog is created with title as {blog.title}."

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)