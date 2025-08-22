from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, sessionLocal
from sqlalchemy.orm import Session
from . import hashing
from .hashing import Hash
from .routers import blog, user, authentication

app = FastAPI()





models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# @app.post('/blog')
# def create():
#     return 'creating'

# @app.post('/blog1')
# def create1(title,body):
#     return {'title':title, 'body':body}

# @app.post('/blog2')
# def create2(request: schemas.Blog):
#     return request

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
# def create(request: schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title = request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog', response_model=List[schemas.ShowBlog],tags=["blogs"])
# def showall(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# def showone(id, response:Response, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return f"Blog with id {id} is not available."
#     return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# def destroy(id, db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if blog.first():
#         blog.delete(synchronize_session=False)
#         db.commit()
#         return f"Deleted blog with id {id}"
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
    

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# def update(id, request: schemas.Blog, db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if blog.first():
#         blog.update({'title': request.title, 'body': request.body})
#         db.commit()
#         db.refresh(blog.first())
#         return 'Updated'
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
    
# @app.post('/user', response_model=schemas.ShowUser, tags=["users"])
# def create_user(request: schemas.User,  db:Session = Depends(get_db)):
    
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user', response_model=schemas.ShowUser, tags=["users"])
# def get_user(id:int,  db:Session = Depends(get_db)):
#     user = db.query(models.User).filter (models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available.")
#     else:
#         return user