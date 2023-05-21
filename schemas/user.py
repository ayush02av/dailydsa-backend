from pydantic import BaseModel
from schemas import question
from typing import List

class AddSubmissionRequest(BaseModel):
    questionID: int
    submissionLink: str

class Submission(BaseModel):
    id: int
    question_link: str
    submission_link: str

class HistoryResponse(BaseModel):
    today: List[Submission]
    previous: List[Submission]