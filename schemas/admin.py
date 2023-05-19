from pydantic import BaseModel

class AddQuestionRequest(BaseModel):
    questionLink: str
    solutionLink: str
    difficultyLevel: int