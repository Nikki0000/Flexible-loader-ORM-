from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Question(Base):
    __tablename__ = 'Question'
    Id = Column(Integer, primary_key=True)
    Type = Column(String, nullable=False)
    QuestionnaireId = Column(Integer, ForeignKey('Questionnaire.Id'), nullable=False)
    Order = Column(Integer, nullable=False)
    CreatedOn = Column(DateTime, default=datetime.utcnow, name='CreatedOn')
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, name='ModifiedOn')
    Name = Column(String, nullable=False)

    # Связь с таблицей Questionnaire
    questionnaire = relationship("Questionnaire", back_populates="questions")
    
    # Связь с таблицей QuestionConfiguration
    configurations = relationship("QuestionConfiguration", back_populates="question")

    answers = relationship("QuestionAnswer", back_populates="question")