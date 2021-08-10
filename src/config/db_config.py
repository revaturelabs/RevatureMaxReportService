from os import environ
from pathlib import Path
import psycopg2


def get_connection():
    """Get the database connection."""
    return psycopg2.connect(
        host=environ["DATABASE_URI"],
        port=environ["PORT"],
        user=environ["DATABASE_USER"],
        password=environ["DATABASE_PASS"],
        database=environ["DATABASE_NAME"])


def get_local_connection():
    return psycopg2.connect(
        host=environ["TEST_URI"],
        port=environ["PORT"],
        user=environ["TEST_USER"],
        password=environ["TEST_PASS"],
        database=environ["DATABASE_NAME"])


def execute_sql(sql: Path):
    with open(sql) as fi:
        with get_local_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(fi.read())
