from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'Detail':{'Name':'Sarang'}}

@app.get('/about')
def about():
    return {'Detail':{'Company': 'Argusoft'}}