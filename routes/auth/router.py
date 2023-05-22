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

    print(details.nickname)
    print(details.email)
    print(details.sub)
    print(details.given_name)
    print(details.family_name)
    print(details.picture)
    
    # raise HTTPException(500, 'internal server error')
    
    # find if user exists
    user = db_session.query(User).filter(User.email == details.email).first()

    if user == None:
        # signup
        user = User(
            username = details.nickname,
            email = details.email,
            sub_password = hash(details.sub),
            first_name = details.given_name if details.given_name != None else "",
            last_name = details.family_name if details.family_name != None else "",
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