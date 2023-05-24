from pydantic import BaseModel
from datetime import datetime

class QuestionResponse(BaseModel):
    id: int
    question_link: str
    solution_link: str
    difficulty_level: int

class QuestionDatedResponse(QuestionResponse):
    created_at: datetime