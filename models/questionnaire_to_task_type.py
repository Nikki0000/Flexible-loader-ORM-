from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class QuestionnaireToTaskType(Base):
    __tablename__ = 'QuestionnaireToTaskType'
    Id = Column(Integer, primary_key=True)
    CreatedOn = Column(DateTime, default=datetime.utcnow, nullable=False)
    ModifiedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    QuestionnaireId = Column(Integer, ForeignKey('Questionnaire.Id'), nullable=False)
    TaskTypeId = Column(Integer, nullable=False)
    Order = Column(Integer, nullable=False)

    questionnaire = relationship("Questionnaire", back_populates="task_types")

    specializations = relationship("QuestionnaireToTaskTypeSpecialization", back_populates="task_types")