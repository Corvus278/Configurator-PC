import json

def json2dict(one_part):
    return json.loads(one_part)

def dict2json(one_part):
    return json.dumps(one_part)

def listdict2json(parts_list):
    new_list = []
    for cortege_part in parts_list:
        new_list.append(json.dumps(cortege_part))
    return new_list

def json2listdict(parts_list):
    new_list = []
    for cortege_part in parts_list:
        new_list.append(json.loads(cortege_part))
    return new_list

def sql2ListDict(ListCortage):
    return [json2dict(cortage[0]) for cortage in ListCortage]
