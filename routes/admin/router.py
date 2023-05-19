from fastapi import APIRouter, HTTPException, status
from schemas import admin
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.user import User
from models.question import Question
from services.db_object_serializer import serialize

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

@router.post('/add', status_code = status.HTTP_202_ACCEPTED)
async def add_question(params: admin.AddQuestionRequest, token = token_depenency, db_session: Session = db_dependency):
    # find user
    user = db_session.query(User)\
        .filter(
            User.email == token['email'],
            User.username == token['username']
        )\
        .first()

    if not user.is_admin:
        raise HTTPException(401, 'Not an admin')
    
    question = Question(
        question_link = params.questionLink,
        solution_link = params.solutionLink,
        difficulty_level = params.difficultyLevel
    )

    db_session.add(question)
    db_session.commit()