from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class QuestionAnswer(Base):
    __tablename__ = 'QuestionAnswer'
    Id = Column(Integer, primary_key=True)
    QuestionId = Column(Integer, ForeignKey('Question.Id'), nullable=False)
    Order = Column(Integer, nullable=False)
    CreatedOn = Column(DateTime, default=datetime.utcnow, nullable=False)
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    Name = Column(String, nullable=False)

    question = relationship("Question", back_populates="answers")