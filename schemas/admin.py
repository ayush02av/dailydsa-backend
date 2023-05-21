from pydantic import BaseModel

class AddQuestionRequest(BaseModel):
    questionLink: str
    solutionLink: str
    difficultyLevel: int

class Submission(BaseModel):
    id: int
    question_link: str
    submission_link: str
    user: str