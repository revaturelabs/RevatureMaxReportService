from dao.dao_helper import cursor_handler


@cursor_handler
def create(
    batch_id,
    week_number,
    exam_grade="null",
    project_grade="null",
    verbal_grade="null",
    other_grade="null",
    presentation_grade="null",
    cursor=None,
):
    cursor.execute(
        """INSERT INTO batch_grades
        (batch_id, week_number, exam_grade, project_grade,
            verbal_grade, other_grade, presentation_grade)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (
            batch_id,
            week_number,
            exam_grade,
            project_grade,
            verbal_grade,
            other_grade,
            presentation_grade,
        ),
    )


@cursor_handler
def read_one(week_number, batch_id, cursor):
    cursor.execute(
        """SELECT * FROM batch_grades
                    WHERE week_number=%s AND batch_id=%s""",
        (week_number, batch_id),
    )
    return cursor.fetchone()


@cursor_handler
def read_all(batch_id, cursor):
    cursor.execute(
        """SELECT * FROM batch_grades
                    WHERE batch_id=%s""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def update(
    batch_id,
    week_number,
    exam_grade="null",
    project_grade="null",
    verbal_grade="null",
    other_grade="null",
    presentation_grade="null",
    cursor=None,
):
    cursor.execute(
        """UPDATE batch_grades
        SET exam_grade=%s, project_grade=%s, verbal_grade=%s,
        other_grade=%s, presentation_grade=%s
        WHERE batch_id=%s AND week_number=%s""",
        (
            batch_id,
            week_number,
            exam_grade,
            project_grade,
            verbal_grade,
            other_grade,
            presentation_grade,
        ),
    )


@cursor_handler
def delete(batch_id, week_number, cursor):
    cursor.execute(
        """DELETE FROM batch_grades
    WHERE batch_id=%s AND week_number=%s""",
        (batch_id, week_number),
    )
