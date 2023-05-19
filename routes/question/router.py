from fastapi import APIRouter, HTTPException, status
from schemas import question
from typing import List
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.question import Question
from services.db_object_serializer import serialize
from datetime import timedelta, datetime

router = APIRouter(
    prefix='/question',
    tags=['question']
)

@router.get('/daily', response_model = List[question.QuestionResponse])
async def daily_question(db_session: Session = db_dependency):
    # find question
    questions = db_session.query(Question)\
        .filter(
            Question.created_at + timedelta(days = 1) > datetime.now()
        )\
        .all()

    return [serialize(question) for question in questions]