from fastapi import APIRouter, HTTPException
from schemas import auth, user
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.user import User
from services.db_object_serializer import serialize

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get('/profile', response_model = auth.EntryResponse)
async def profile(token = token_depenency, db_session: Session = db_dependency):
    # find user
    user = db_session.query(User)\
        .filter(
            User.email == token['email'],
            User.username == token['username']
        )\
        .first()

    return serialize(user)