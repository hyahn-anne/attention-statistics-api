from datetime import date as date_type
from pydantic import BaseModel, Field
from pydantic.class_validators import validator
from sqlalchemy import orm


class AttentionDetailBase(BaseModel):
    daily_attention_score: float
    class Config:
        orm_mode = True


class AttentionScoreAverage(AttentionDetailBase):
    daily_attention_score: float = Field(alias="average_attention_score")
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class AssessmentBase(BaseModel):
    daily_assessment_type_code: int
    count: int
    class Config:
        orm_mode = True


class AttentionSummary(BaseModel):
    date: date_type
    daily_problem_count: int
    daily_accuracy_count: int
    daily_slow_speed_count: int
    daily_mistake_count: int
    daily_random_answer_count: int
    class Config:
        orm_mode = True


class MaxPredictAccuracyLessonInfo(BaseModel):
    lesson_id: int
    lesson_title: str
    chapter_id: int
    lesson_predict_accuracy: float
    class Config:
        orm_mode = True