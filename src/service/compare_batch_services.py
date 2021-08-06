from src.dao import compare_batch_dao

def get_batch_by_id(batch_id, productionDB=True):
    return compare_batch_dao.get_batch_by_id(batch_id, productionDB)

def get_batches_with_same_skill(skill, start_date, productionDB=True):
    return compare_batch_dao.get_batches_with_same_skill(skill, start_date, productionDB)

def batch_total_avg(batch_id, productionDB=True):
    return float(compare_batch_dao.batch_total_avg(batch_id, productionDB)[0])

def batch_weekly_avg(batch_id, week, productionDB=True):
    return compare_batch_dao.batch_weekly_avg(batch_id, week, productionDB)[0]
