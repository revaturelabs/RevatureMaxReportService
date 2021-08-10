from dao.dao_helper import cursor_handler


@cursor_handler
def select_name_by_email(associate_email, cursor):
    cursor.execute("""
        SELECT firstname || ' ' || lastname AS name FROM associate
        WHERE email LIKE %s
    """, (associate_email,))
    return cursor.fetchone()
