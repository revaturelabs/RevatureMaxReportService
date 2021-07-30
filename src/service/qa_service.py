def parseTraineeJson(json):
    return_dict = {}

    for x in json:
        return_dict[x['week']] = x

    return return_dict
