from src.dao import qc_dao as dao


def get_qc_info_trainee(associate_id):
    return_dict = {}

    result = dao.select_qc_info_by_associate_id(associate_id)
    for x in result:
        content = x[0]
        week = x[1]
        tech_status = x[2]
        batch_id = x[3]
        batch_average = dao.select_qc_batch_average_by_week(batch_id, week)[0]

        row_dict = {'type': 'QC', 'score': tech_status, 'notes': content, 'average': batch_average,
                    'week': f"Week {week}"}

        return_dict[week] = row_dict

    return return_dict
