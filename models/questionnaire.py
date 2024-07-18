from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Questionnaire(Base):
    __tablename__ = 'Questionnaire'
    Id = Column(Integer, primary_key=True)
    CreatedOn = Column(DateTime, default=datetime.utcnow, name='CreatedOn')
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, name='ModifiedOn')
    Name = Column(String, nullable=False, name='Name')

    questions = relationship("Question", back_populates="questionnaire")

    task_types = relationship("QuestionnaireToTaskType", back_populates="questionnaire")

    specializations = relationship("QuestionnaireToTaskTypeSpecialization", back_populates="questionnaire")