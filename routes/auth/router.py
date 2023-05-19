from fastapi import APIRouter, HTTPException
from schemas import auth
from dependency import db_dependency
from sqlalchemy.orm import Session
from models.user import User
import jwt

from services.db_object_serializer import serialize
from services.password_hasher import hash
from services.token_generator import generate

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/entry', response_model = auth.EntryResponse)
async def entry(params: auth.EntryRequest, db_session: Session = db_dependency):
    details = jwt.decode(params.token, options={"verify_signature": False})
    details = auth.TempToken(**details)
    
    # find if user exists
    user = db_session.query(User).filter(User.email == details.email).first()

    if user == None:
        # signup
        user = User(
            username = details.nickname,
            email = details.email,
            sub_password = hash(details.sub),
            first_name = details.given_name,
            last_name = details.family_name,
            picture = details.picture
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        
        user = serialize(user)
        user['token'] = generate(user)
        
        return user
    
    else:
        # login
        if user.sub_password != hash(details.sub):
            raise HTTPException(401, 'Incorrect Password')
        
        user = serialize(user)
        user['token'] = generate(user)
        
        return user