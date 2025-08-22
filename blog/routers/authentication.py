from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas, models, database
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import authentication
from ..hashing import Hash

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: schemas.Login, db:Session = Depends(get_db)):
    return authentication.Login(request, db)