import sys
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
from pydantic.main import create_model
from sqlalchemy import Column, Integer, Float, Date, NVARCHAR
from database.db import BaseModel


class AttentionDetail(BaseModel):
    __tablename__ = "attention_detail"
    user_id = Column(Integer, primary_key=True)
    created_yyyymmdd = Column(Date, primary_key=True)
    daily_attention_score = Column(Float)
    daily_assessment_type_code = Column(Integer)
    daily_problem_count = Column(Integer)
    daily_accuracy_count = Column(Integer)
    daily_slow_speed_count = Column(Integer)
    daily_mistake_count = Column(Integer)
    daily_random_answer_count = Column(Integer)


class AttentionGraph(BaseModel):
    __tablename__ = "attention_graph"
    problem_logs_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_yyyymmdd = Column(Date)
    problem_id = Column(Integer)
    accuracy = Column(Integer)
    real_elapsed_time = Column(Float)


class AttentionPredictLesson(BaseModel):
    __tablename__ = "attention_predict_lesson"
    user_id = Column(Integer, primary_key=True)
    created_yyyymmdd = Column(Date, primary_key=True)
    lesson_id = Column(Integer)
    lesson_subjective_difficulty = Column(Float)
    lesson_title = Column(NVARCHAR(length=512))
    chapter_id = Column(Integer)
    lesson_predict_accuracy = Column(Float)
