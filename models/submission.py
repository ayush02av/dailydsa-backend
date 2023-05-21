from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Submission(Base):
    __tablename__ = "submission"

    id = Column(Integer, primary_key = True, index = True, nullable = False)
    user_id = Column(Integer)
    question_id = Column(Integer)
    submission_link = Column(String(255))

    created_at = Column(DateTime(timezone = True), server_default = func.now())