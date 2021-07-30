def parseTraineeJson(json):
    return_dict = {}

    for x in json:
        return_dict[x['week']] = x

    return return_dict


def parseBatchJson(json):
    return_dict = {}

    for x in json:
        return_dict[x['week']] = x

    return return_dict


def parseBatchIndividualJson(json):
    return_dict = {}

    for x in json:
        return_dict[f"{x['associateId']} {x['week']}"] = x

    return return_dict
