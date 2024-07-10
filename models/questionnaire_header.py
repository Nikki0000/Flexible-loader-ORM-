from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class QuestionnaireHeader(Base):
    __tablename__ = 'QuestionnaireHeader'
    Id = Column(Integer, primary_key=True)
    CreatedOn = Column(DateTime, default=datetime.utcnow, name='CreatedOn')
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, name='ModifiedOn')
    Name = Column(String, nullable=False, name='Name')
    Visible = Column(Boolean, default=True, name='Visible')
    Position = Column(Integer, nullable=False, name='Position')


    configurations = relationship("QuestionConfiguration", back_populates="questionnaire_header")