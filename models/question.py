from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key = True, index = True, nullable = False)
    question_link = Column(String(255), nullable = False)
    solution_link = Column(String(255), )
    difficulty_level = Column(Integer)

    created_at = Column(DateTime(timezone = True), server_default = func.now())