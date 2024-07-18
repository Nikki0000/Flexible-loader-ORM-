from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class QuestionnaireToTaskTypeSpecialization(Base):
    __tablename__ = 'QuestionnaireToTaskTypeSpecialization'
    Id = Column(Integer, primary_key=True)
    CreatedOn = Column(DateTime, default=datetime.utcnow, nullable=False)
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    QuestionnaireId = Column(Integer, ForeignKey('Questionnaire.Id'), nullable=False)
    SpecializationId = Column(Integer, nullable=False)
    QuestionnaireToTaskTypeId = Column(Integer, ForeignKey('QuestionnaireToTaskType.Id'), nullable=False)

    questionnaire = relationship("Questionnaire", back_populates="specializations")
    task_types = relationship("QuestionnaireToTaskType", back_populates="specializations")