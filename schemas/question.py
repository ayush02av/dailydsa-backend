from pydantic import BaseModel

class QuestionResponse(BaseModel):
    id: int
    question_link: str
    solution_link: str
    difficulty_level: int