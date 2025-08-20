from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post('/blog')
def create():
    return 'creating'

@app.post('/blog1')
def create1(title,body):
    return {'title':title, 'body':body}

@app.post('/blog2')
def create2(request: schemas.Blog):
    return request
