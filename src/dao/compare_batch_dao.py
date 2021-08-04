from src.config.db_config import get_connection, get_local_connection
from datetime import datetime

def get_batch_by_id(batch_id, productionDB=True):
    try:
        if productionDB:
            conn = get_connection()
        else:
            conn = get_local_connection()
        cur = conn.cursor()
        SQL = """SELECT skill, startdate FROM report_batch WHERE batchid = %s"""
        cur.execute(SQL, (str(batch_id),))
        return cur.fetchone()
    finally:
        conn.close()

def get_batches_with_same_skill(skill, start_date, productionDB=True):
    try:
        if productionDB:
            conn = get_connection()
        else:
            conn = get_local_connection()
        cur = conn.cursor()
        SQL = """SELECT batchid FROM report_batch WHERE skill = %s AND %s > startdate"""
        cur.execute(SQL, (skill, start_date))
        return cur.fetchall()
    finally:
        conn.close()

def batch_total_avg(batch_id, productionDB=True):
    try:
        if productionDB:
            conn = get_connection()
        else:
            conn = get_local_connection()
        cur = conn.cursor()
        SQL = """SELECT SUM(average)/ COUNT(average) FROM batch_grades WHERE batch_id = %s"""
        cur.execute(SQL, (batch_id,))
        return cur.fetchone()
    finally:
        conn.close()

def batch_weekly_avg(batch_id, week, productionDB=True):
    try:
        if productionDB:
            conn = get_connection()
        else:
            conn = get_local_connection()
        cur = conn.cursor()
        SQL = """SELECT SUM(score)/COUNT(score) FROM report_on_assessment WHERE traineeid = %s AND week = %s"""
        cur.execute(SQL, (batch_id, week))
        return cur.fetchone()
    finally:
        conn.close()