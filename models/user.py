from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, index = True, nullable = False)
    username = Column(String(100), unique = True, index = True, nullable = False)
    email = Column(String(100), unique = True, index = True, nullable = False)
    sub_password = Column(String(500))
    first_name = Column(String(100), nullable = False)
    last_name = Column(String(100), nullable = False)
    picture = Column(String(255))
    last_submission = Column(DateTime(timezone = True))
    is_admin = Column(Boolean, nullable = False, default=False)

    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())