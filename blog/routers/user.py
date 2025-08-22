from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    tags=["users"], 
    prefix='/user'
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,  db:Session = Depends(get_db)):
    return user.my_user(request, db)
    

@router.get('/user', response_model=schemas.ShowUser)
def get_user(id:int,  db:Session = Depends(get_db)):
    return user.find_user(id, db)