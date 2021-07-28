from os import environ
import psycopg2


def get_connection():
    """Get the database connection."""
    return psycopg2.connect(
        host=environ["DATABASE_URI"],
        port=environ["PORT"],
        user=environ["DATABASE_USER"],
        password=environ["DATABASE_PASS"],
        database=environ["DATABASE"])


def get_local_connection():
    return psycopg2.connect(
        host=environ["TEST_URI"],
        port=environ["PORT"],
        user=environ["TEST_USER"],
        password=environ["TEST_PASS"],
        database=environ["DATABASE"])


def reset_db(conn):
    """Ensure the db has the appropriate tables.
        conn -- the psycopg2 connection
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            pass
        conn.commit()
