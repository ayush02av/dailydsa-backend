from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Submission(Base):
    __tablename__ = "submission"

    id = Column(Integer, primary_key = True, index = True, nullable = False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete = "CASCADE"))
    question_id = Column(Integer, ForeignKey("question.id", ondelete = "CASCADE"))
    submission_link = Column(String)

    created_at = Column(DateTime(timezone = True), server_default = func.now())