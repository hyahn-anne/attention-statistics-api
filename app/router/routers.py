from typing import List
from datetime import date as date_type, timedelta
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import crud, schemas
from database.db import init_database, get_session
from common.utils import get_ndays_ago


init_database()
router = APIRouter()


@router.get('/attention-score/{user_id}', response_model=schemas.AttentionDetailBase, tags=['attention_detail'])
async def get_attention_score(user_id: int, date: date_type, session: Session = Depends(get_session)):
    result = crud.get_attention_score(session=session, user_id=user_id, date=date)
    return result


@router.get('/attention-score/average/{user_id}', response_model=schemas.AttentionScoreAverage, tags=['attention_detail'])
async def get_average_attention_score(user_id: int, date: date_type, session: Session = Depends(get_session)):
    start_date = get_ndays_ago(date, 2)
    result = crud.get_avg_attention_score(session=session, user_id=user_id, start_date=start_date, end_date=date)
    return result


@router.get('/assessment/type-codes/{user_id}', response_model=List[schemas.AssessmentBase], tags=['attention_detail'])
async def get_assessment_type_codes(user_id: int, date: date_type, session: Session = Depends(get_session)):
    result = crud.get_assessment_type_code_log(session=session, user_id=user_id, date=date)
    return result


@router.get('/problem-logs/{user_id}', response_model=List[schemas.AttentionSummary], tags=['attention_detail'])
async def get_attention_summary(user_id: int, date: date_type, session: Session = Depends(get_session)):
    start_date = get_ndays_ago(date, 2)
    result = crud.get_attention_summary_for_threedays(session=session, user_id=user_id,
                                                      start_date=start_date, end_date=date)
    return result


@router.get('/wrong-problems/{user_id}',
    response_class=JSONResponse,
    responses={
        200: {
            'content': {
                'application/json': {
                    'example': [{
                        'problem_id': 0,
                        'real_elapsed_time': 0.0
                    }]
                }
            }
        }
    },
    tags=['attention_graph'])
async def get_wrong_problems(user_id: int, date: date_type, session: Session = Depends(get_session)):
    result = crud.get_wrong_problems(session=session, user_id=user_id, date=date)
    print(result)
    return JSONResponse(result)


@router.get('/high-difficulty-users',
    response_class=JSONResponse,
    responses={
        200: {
            'content': {
                'application/json': {
                    'example': [{
                        'user_id': 0,
                        'lesson_id': 0
                    }]
                }
            }
        }
    },
    tags=['attention_predict_lesson'])
async def get_high_difficulty_users(date: date_type, session: Session = Depends(get_session)):
    result = crud.get_high_difficulty_users(session=session, date=date)
    return JSONResponse(result)


@router.get('/max-predic-accuracy-lesson/{user_id}',
        response_model=schemas.MaxPredictAccuracyLessonInfo,
        tags=['attention_predict_lesson'])
async def get_max_predict_accuracy_lesson_info(user_id: int, date: date_type, session: Session = Depends(get_session)):
    result = crud.get_max_predict_accuracy_lesson(session=session, user_id=user_id, date=date)
    return result
