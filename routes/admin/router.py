from fastapi import APIRouter, HTTPException, status
from schemas import admin
from typing import List
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.user import User
from models.question import Question
from models.submission import Submission
from datetime import datetime, timedelta
from sqlalchemy import extract

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
        question_link = params.questionLink.rstrip('/'),
        solution_link = params.solutionLink.rstrip('/'),
        difficulty_level = params.difficultyLevel
    )

    db_session.add(question)
    db_session.commit()

@router.get('/history', response_model = List[admin.Submission])
async def history(token = token_depenency, db_session: Session = db_dependency):
    # find user
    user = db_session.query(User)\
        .filter(
            User.email == token['email'],
            User.username == token['username']
        )\
        .first()

    if not user.is_admin:
        raise HTTPException(401, 'Not an admin')
    
    submissions = list()
    
    for q, s, u in db_session.query(Question, Submission, User).filter(
        Submission.question_id == Question.id,
        Submission.user_id == User.id,
        datetime.utcnow().day == extract('day', Question.created_at),
        datetime.utcnow().month == extract('month', Question.created_at),
        datetime.utcnow().year == extract('year', Question.created_at)
    ).all():
        submissions.append({
            'id': s.id,
            'question_link': q.question_link,
            'submission_link': s.submission_link,
            'user': u.username,
            'created_at': s.created_at
        })
        
    return submissions