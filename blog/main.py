from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(engine)

# @app.post('/blog')
# def create():
#     return 'creating'

# @app.post('/blog1')
# def create1(title,body):
#     return {'title':title, 'body':body}

# @app.post('/blog2')
# def create2(request: schemas.Blog):
#     return request

@app.post('/blog')
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog