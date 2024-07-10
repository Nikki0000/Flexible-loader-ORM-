from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class QuestionConfiguration(Base):
    __tablename__ = 'QuestionConfiguration'
    Id = Column(Integer, primary_key=True)
    CreatedOn = Column(DateTime, default=datetime.utcnow, name='CreatedOn')
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, name='ModifiedOn')
    QuestionId = Column(Integer, ForeignKey('Question.Id'), nullable=False, name='QuestionId')
    QuestionnaireHeaderId = Column(Integer, ForeignKey('QuestionnaireHeader.Id'), nullable=False, name='QuestionnaireHeaderId')
    RowNumber = Column(Integer, nullable=False, name='RowNumber')

    # Связь с таблицей Question
    question = relationship("Question", back_populates="configurations")
    
    # Связь с таблицей QuestionnaireHeader
    questionnaire_header = relationship("QuestionnaireHeader", back_populates="configurations")