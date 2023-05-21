from fastapi import APIRouter, status
from schemas import auth, user
from dependency import db_dependency, token_depenency
from sqlalchemy.orm import Session
from models.user import User
from models.question import Question
from models.submission import Submission
from services.db_object_serializer import serialize
from sqlalchemy import extract
from datetime import datetime

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

@router.post('/add', status_code = status.HTTP_202_ACCEPTED)
async def add_submission(params: user.AddSubmissionRequest, token = token_depenency, db_session: Session = db_dependency):
    # find user
    user = db_session.query(User)\
        .filter(
            User.email == token['email'],
            User.username == token['username']
        )\
        .first()
    
    submission = Submission(
        user_id = user.id,
        question_id = params.questionID,
        submission_link = params.submissionLink
    )

    db_session.add(submission)
    db_session.commit()
    
@router.get('/history', response_model = user.HistoryResponse)
async def history(token = token_depenency, db_session: Session = db_dependency):
    today = list()
    previous = list()
    
    now_date = datetime.now().date()
    
    for q, s in db_session.query(Question, Submission).filter(
        Submission.user_id == token['id'],
        Submission.question_id == Question.id
    ).all():
        submission = {
            'id': s.id,
            'question_link': q.question_link,
            'submission_link': s.submission_link,
            'created_at': s.created_at
        }
        
        if submission['created_at'].date() == now_date:
            today.append(submission)
        else:
            previous.append(submission)
        
    return {
        'today': today,
        'previous': previous
    }