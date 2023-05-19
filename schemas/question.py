from pydantic import BaseModel

class QuestionResponse(BaseModel):
    question_link: str
    solution_link: str
    difficulty_level: int