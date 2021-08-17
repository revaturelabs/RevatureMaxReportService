from dao.dao_helper import cursor_handler


@cursor_handler
def create_new_associate(email, salesforceId, firstname, lastname, batch_id, cursor):
    cursor.execute("""INSERT INTO associate
    VALUES (%s, %s, %s, %s, %s)
    """, (email, salesforceId, firstname, lastname, batch_id))


@cursor_handler
def select_name_by_email(associate_email, cursor):
    cursor.execute("""
        SELECT firstname || ' ' || lastname AS name FROM associate
        WHERE email LIKE %s
    """, (associate_email,))
    return cursor.fetchone()
