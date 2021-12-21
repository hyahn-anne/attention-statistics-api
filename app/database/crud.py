from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from model.models import AttentionDetail, AttentionGraph, AttentionPredictLesson
from common.utils import convert_tuplelist_to_dict


def get_attention_score(session: Session, user_id: int, date: date):
    """
    return daily attention score by user_id and date

    parameters :
        user_id (int): student id in database
        date (date): specific date from query string

    returns :
        int: daily attention score
    """
    query = session.query(AttentionDetail.daily_attention_score).filter(
        AttentionDetail.user_id == user_id,
        AttentionDetail.created_yyyymmdd == date)
    result = query.first()
    return result


def get_avg_attention_score(session: Session, user_id: int, start_date: date, end_date: date):
    """
    return average of daily attention scores for last 3 days by user_id and date

    parameters :
        user_id (int): student id in database
        start_date (date): the date of 2 days ago from end_date
        end_date (date): specific date from query string

    returns :
        float: average of daily attention score for last 3 days
    """
    query = session.query(
        func.avg(AttentionDetail.daily_attention_score).label('daily_attention_score'))
    query = query.filter(
        AttentionDetail.user_id == user_id,
        AttentionDetail.created_yyyymmdd.between(start_date, end_date))
    result = query.first()
    return result


def get_assessment_type_codes(session: Session, user_id: int, date: date):
    """
    return assessment type code and the number of code

    parameters :
        user_id (int): student id in database
        date (datetime): specific date from query string

    returns ::
        dict:
        {
            'daily_assessment_type_code': type_code(int),
            'count': type code count(int)
        }
    """
    query = session.query(
        AttentionDetail.daily_assessment_type_code,
        func.count(AttentionDetail.daily_assessment_type_code).label('count'))
    query = query.filter(
        AttentionDetail.user_id == user_id,
        AttentionDetail.created_yyyymmdd == date).group_by(AttentionDetail.daily_assessment_type_code)
    result = query.all()
    return result


def get_problem_logs(session: Session, user_id: int, start_date: date, end_date: date):
    """
    return attention detail summary for last three days

    parameters :
        user_id (int): student id in database
        start_date (date): the date of 2 days ago from end_date
        end_date (date): specific date from query string

    returns ::
        dict:
        {
            'date': date,
            'daily_problem_count': int,
            'daily_accuracy_count': int,
            'daily_slow_speed_count': int,
            'daily_mistake_count': int,
            'daily_random_answer_count': int
        }
    """
    query = session.query(
        AttentionDetail.created_yyyymmdd.label('date'),
        AttentionDetail.daily_problem_count,
        AttentionDetail.daily_accuracy_count,
        AttentionDetail.daily_slow_speed_count,
        AttentionDetail.daily_mistake_count,
        AttentionDetail.daily_random_answer_count)
    query = query.filter(
        AttentionDetail.user_id == user_id,
        AttentionDetail.created_yyyymmdd.between(start_date, end_date))
    result = query.all()
    return result


def get_wrong_problems(session: Session, user_id: int, date: date):
    """
    return id of wrong problems and elapsed time

    parameters :
        user_id (int): student id in database
        date (datetime): specific date from query string

    returns ::
        dict:
        {
            'problem_id': int,
            'real_elapsed_time': list
        }
    """
    query = session.query(
        AttentionGraph.problem_id,
        AttentionGraph.real_elapsed_time
    )
    query = query.filter(
        AttentionGraph.user_id == user_id,
        AttentionGraph.created_yyyymmdd == date,
        AttentionGraph.accuracy == 0
    )
    result = query.all()
    dict_result = convert_tuplelist_to_dict(
        result,
        [AttentionGraph.problem_id.name, AttentionGraph.real_elapsed_time.name]
    )
    return dict_result


def get_high_difficulty_users(session: Session, date: date, difficulty: float = 4.0):
    """
    return user and lesson id of level 4 or higher

    parameters :
        date (datetime): specific date from query string

    returns ::
        dict:
        {
            'user_id': int,
            'lesson_id': list
        }
    """
    query = session.query(
        AttentionPredictLesson.user_id,
        AttentionPredictLesson.lesson_id
    )
    query = query.filter(
        AttentionPredictLesson.created_yyyymmdd == date,
        AttentionPredictLesson.lesson_subjective_difficulty >= difficulty
    ).order_by(AttentionPredictLesson.lesson_subjective_difficulty)
    result = query.all()
    dict_result = convert_tuplelist_to_dict(
        result,
        [AttentionPredictLesson.user_id.name, AttentionPredictLesson.lesson_id.name]
    )
    return dict_result


def get_max_predict_accuracy_lesson(session: Session, user_id: int, date: date):
    """
    return lession id, lesson title, chapter id and lesson predict accuracy
    with max predict accruracy

    parameters :
        user_id (int): student id in database
        date (datetime): specific date from query string

    returns ::
        dict:
        {
            'lesson_id': int,
            'lesson_title': str,
            'chapter_id': int,
            'lesson_predict_accuracy': float
        }
    """
    subquery = session.query(
        func.max(AttentionPredictLesson.lesson_predict_accuracy)
    ).filter(
        AttentionPredictLesson.user_id == user_id,
        AttentionPredictLesson.created_yyyymmdd == date
    ).subquery()

    query = session.query(
        AttentionPredictLesson.lesson_id,
        AttentionPredictLesson.lesson_title,
        AttentionPredictLesson.chapter_id,
        AttentionPredictLesson.lesson_predict_accuracy
    ).filter(
        AttentionPredictLesson.lesson_predict_accuracy.in_(subquery),
        AttentionPredictLesson.user_id == user_id
    )

    result = query.first()
    print(result)
    return result
