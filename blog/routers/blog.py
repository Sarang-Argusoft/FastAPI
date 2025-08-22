from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router=APIRouter(
    tags=["blogs"],
    prefix="/blog"
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    return blog.create(request, db)



@router.get('/', response_model=List[schemas.ShowBlog])
def showall(db:Session = Depends(get_db)):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def showone(id: int, response:Response, db:Session = Depends(get_db)):
    return blog.show(db, id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session = Depends(get_db)):
    return blog.destroy(id, db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id, db, request)