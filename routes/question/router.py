from fastapi import APIRouter
from schemas import question
from typing import List
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.question import Question
from services.db_object_serializer import serialize
from datetime import datetime
from sqlalchemy import extract

router = APIRouter(
    prefix='/question',
    tags=['question']
)

@router.get('/daily', response_model = List[question.QuestionResponse])
async def daily_question(db_session: Session = db_dependency):
    # find question
    questions = db_session.query(Question)\
        .filter(
                datetime.now().day == extract('day', Question.created_at),
                datetime.now().month == extract('month', Question.created_at),
                datetime.now().year == extract('year', Question.created_at)
        )\
        .all()

    return [serialize(question) for question in questions]