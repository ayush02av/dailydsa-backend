from database import SessionLocal, engine
from fastapi import Depends
from models import user, question
from typing_extensions import Annotated
import jwt
from fastapi import Header, HTTPException, Depends
from config import config

user.Base.metadata.create_all(bind = engine)
question.Base.metadata.create_all(bind = engine)

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
db_dependency = Depends(get_db_session)

def verify_token(token: Annotated[str, Header()]):
    try:
        data = jwt.decode(token, config.AUTH_TOKEN_SECRET, algorithms=[ config.AUTH_TOKEN_ALGORITHM ])
        yield data
    except Exception as exception:
        raise HTTPException(400, exception.__str__())
    
token_depenency = Depends(verify_token)