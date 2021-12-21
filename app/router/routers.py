from typing import List
from datetime import date as date_type, datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import crud, schemas
from database.db import init_database, get_session
from common.utils import get_ndays_ago


init_database()
router = APIRouter()


def check_date_format(date: str):
    try:
        formatted_date = datetime.strptime(date, '%Y-%m-%d')
        print(formatted_date)
        return formatted_date
    except ValueError as e:
        raise HTTPException(status_code=422, detail='Invalid date format. Date format is yyyy-mm-dd')


@router.get('/attention-score/{user_id}', response_model=schemas.AttentionDetailBase, tags=['attention_detail'])
async def get_attention_score(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    result = crud.get_attention_score(session=session, user_id=user_id, date=formatted_date)
    return result


@router.get('/attention-score/average/{user_id}', response_model=schemas.AttentionScoreAverage, tags=['attention_detail'])
async def get_average_attention_score(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    start_date = get_ndays_ago(formatted_date, 2)
    result = crud.get_avg_attention_score(session=session, user_id=user_id, start_date=start_date, end_date=formatted_date)
    return result


@router.get('/assessment/type-codes/{user_id}', response_model=List[schemas.AssessmentBase], tags=['attention_detail'])
async def get_assessment_type_codes(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    result = crud.get_assessment_type_code_log(session=session, user_id=user_id, date=formatted_date)
    return result


@router.get('/problem-logs/{user_id}', response_model=List[schemas.AttentionSummary], tags=['attention_detail'])
async def get_attention_summary(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    start_date = get_ndays_ago(formatted_date, 2)
    result = crud.get_attention_summary_for_threedays(session=session, user_id=user_id,
                                                      start_date=start_date, end_date=formatted_date)
    return result


@router.get('/wrong-problems/{user_id}',
    response_class=JSONResponse,
    responses={
        200: {
            'content': {
                'application/json': {
                    'example': [{
                        'problem_id': 0,
                        'real_elapsed_time': [0.1, 0.2]
                    }]
                }
            }
        }
    },
    tags=['attention_graph'])
async def get_wrong_problems(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    result = crud.get_wrong_problems(session=session, user_id=user_id, date=formatted_date)
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
                        'lesson_id': [0, 1]
                    }]
                }
            }
        }
    },
    tags=['attention_predict_lesson'])
async def get_high_difficulty_users(date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    result = crud.get_high_difficulty_users(session=session, date=formatted_date)
    return JSONResponse(result)


@router.get('/max-predict-accuracy-lesson/{user_id}',
        response_model=schemas.MaxPredictAccuracyLessonInfo,
        tags=['attention_predict_lesson'])
async def get_max_predict_accuracy_lesson_info(user_id: int, date: str, session: Session = Depends(get_session)):
    formatted_date = check_date_format(date)
    result = crud.get_max_predict_accuracy_lesson(session=session, user_id=user_id, date=formatted_date)
    return result
