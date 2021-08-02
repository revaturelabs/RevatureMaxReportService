def parseTraineeJson(json_ind, json_batch):
    return_dict = {}

    row = 1
    batch_list = 0

    for x in json_ind:

        row_dict = {'Type': 'QC', 'Score': x['technicalStatus'], 'Notes': x['content'], 'Average': json_batch[batch_list]['technicalStatus']}

        return_dict[x['week']] = row_dict
        row = row + 1
        batch_list = batch_list + 1

    return return_dict


def parseBatchJson(json):
    return_dict = {}

    for x in json:
        return_dict[x['week']] = x

    return return_dict


def getbatchID(json):
    return json[0]['batchId']


def parseBatchIndividualJson(json):
    return_dict = {}
    row = 1
    for x in json:
        row_dict = {'associateId': x['associateId'], 'batchID': x['batchId'], 'content': x['content'],
                    'technicalStatus': x['technicalStatus'], 'week': x['week']}
        return_dict[row] = row_dict
        row = row + 1

    return return_dict
