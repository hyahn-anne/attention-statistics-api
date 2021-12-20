SELECT
	daily_attention_score
FROM
	attention_detail
WHERE
	user_id = "13312" AND created_yyyymmdd = "2021-12-06"


SELECT
	AVG(daily_attention_score)
FROM
	attention_detail
WHERE
	user_id = "202329"
	AND
	created_yyyymmdd BETWEEN DATE_SUB("2021-12-09", INTERVAL 2 DAY) AND "2021-12-09"


SELECT
	daily_assessment_type_code,
	COUNT(daily_assessment_type_code)
FROM
	attention_detail
WHERE
	user_id = "63420"
	AND
	created_yyyymmdd = "2021-12-07"
GROUP BY
	daily_assessment_type_code


SELECT
    created_yyyymmdd,
	daily_problem_count,
	daily_accuracy_count,
	daily_slow_speed_count,
	daily_mistake_count,
	daily_random_answer_count
FROM
	attention_detail
WHERE
	user_id = "202329"
	AND
	created_yyyymmdd BETWEEN DATE_SUB("2021-12-09", INTERVAL 2 DAY) AND "2021-12-09"


SELECT
	problem_id,
	real_elapsed_time
FROM
	attention_graph
WHERE
	user_id = "202329"
	AND
	created_yyyymmdd = "2021-12-07"
	AND
	accuracy = 0
	

SELECT
	user_id,
	lesson_id,
	lesson_subjective_difficulty 
FROM
	attention_predict_lesson
WHERE
	lesson_subjective_difficulty >= 4
	AND
	created_yyyymmdd = "2021-12-07"


SELECT
	pa.lesson_id,
	pa.lesson_title,
	pa.chapter_id,
	MAX(pa.lesson_predict_accuracy) as lesson_predict_accuracy
FROM
	(SELECT
		lesson_id,
		lesson_title,
		chapter_id,
		lesson_predict_accuracy
	 FROM
		attention_predict_lesson
	 WHERE
		user_id = "13435"
		AND
		created_yyyymmdd = "2021-12-07") as pa


SELECT
	lesson_id,
	lesson_title,
	chapter_id,
	lesson_predict_accuracy
FROM
	attention_predict_lesson
WHERE
	lesson_predict_accuracy =
		(
			SELECT
				max(lesson_predict_accuracy)
			FROM
				attention_predict_lesson
			WHERE
				user_id = "202329"
			AND
			created_yyyymmdd = "2021-12-07"
		)
	AND
	user_id = "202329"



