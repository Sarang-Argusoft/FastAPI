from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

def Login(request: schemas.Login, db:Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials.")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password.")
    return user