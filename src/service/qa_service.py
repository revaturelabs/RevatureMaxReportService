from src.dao import qc_dao as dao


# def parseTraineeJson(json_ind, json_batch):
#     row_dict = {}
#     return_dict = {}
#
#     week = 1
#
#     for x in json_ind:
#         for y in json_batch:
#             if int(y['week']) is week:
#                 row_dict = {'type': 'QC', 'score': x['technicalStatus'], 'notes': x['content'], 'average': y['technicalStatus'], 'week': f"Week {x['week']}"}
#
#         return_dict[x['week']] = row_dict
#         week = week + 1
#
#     return return_dict
#
#
# def getbatchID(json):
#     return json[0]['batchId']
#

def get_qc_info(associate_id):
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


