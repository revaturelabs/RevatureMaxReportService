from src.dao.dao_helper import cursor_handler

@cursor_handler
def select_qc_info_by_associate_id(associate_id, cursor):
    cursor.execute(
        """select content, week, technical_status, batch_id from report_qc_note where associate_id=%s""",
        [associate_id]
    )
    return cursor.fetchall()

@cursor_handler
def select_qc_batch_average_by_week(batch_id, week, cursor):
    cursor.execute(
        """SELECT technical_status FROM report_qc_batch_note WHERE batch_id=%s AND week=%s""",
        [batch_id, week]
    )
    return cursor.fetchone()
