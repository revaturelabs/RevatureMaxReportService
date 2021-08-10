from dao.dao_helper import cursor_handler


@cursor_handler
def create_existing(
    grade_id, batch_id, email, category, score, week, grade_weight, cursor
):
    cursor.execute(
        """INSERT INTO report_on_category
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (grade_id, batch_id, email, category, score, week, grade_weight),
    )


@cursor_handler
def create_new(batch_id, email, category, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_category
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (batch_id, email, category, score, week, grade_weight),
    )


@cursor_handler
def select_by_email_category_week(email, category, week, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s AND category LIKE %s AND week = %s""",
        (email, category, week),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email_category(email, category, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s AND category LIKE %s""",
        (email, category),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email(email, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s""",
        (email,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch(batch_id, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_averages(batch_id, cursor):
    cursor.execute(
        """SELECT email, category, AVG(score), SUM(grade_weight) FROM report_on_category
        WHERE batch_id LIKE %s
        GROUP BY email, category""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_assessment(batch_id, category, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s AND category LIKE %s""",
        (batch_id, category),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_max_grade(batch_id, max_grade, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s AND score < %s""",
        (batch_id, max_grade),
    )
    return cursor.fetchall()


@cursor_handler
def select_all_categories(cursor):
    cursor.execute("""SELECT DISTINCT category FROM report_on_category""")
    return cursor.fetchall()


@cursor_handler
def select_by_batch_category(batch_id, category_type, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s AND category LIKE %s""",
        (batch_id, category_type),
    )
    return cursor.fetchall()


@cursor_handler
def select_batch_averages_weekly(batch_id, cursor):
    cursor.execute(
        """SELECT SUM(score * grade_weight) / SUM(grade_weight), category, week
        FROM report_on_category
        WHERE batch_id LIKE %s
        GROUP BY week, category""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_categorical_averages_by_email_weekly(email, cursor):
    cursor.execute(
        """SELECT SUM(score * grade_weight) / SUM(grade_weight), category, week
        FROM report_on_category
        WHERE email LIKE %s AND grade_weight > 0
        GROUP BY week, category""",
        (email,),
    )
    return cursor.fetchall()


@cursor_handler
def select_batch_average_weekly(batch_id, cursor):
    cursor.execute(
        """SELECT SUM(score * grade_weight) / SUM(grade_weight), category, week
        FROM report_on_category
        WHERE batch_id LIKE %s
        GROUP BY week, category""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_categorical_averages_by_email_weekly(email, cursor):
    cursor.execute(
        """SELECT SUM(score * grade_weight) / SUM(grade_weight), category, week
        FROM report_on_category
        WHERE email LIKE %s AND grade_weight > 0
        GROUP BY week, category""",
        (email,),
    )
    return cursor.fetchall()
