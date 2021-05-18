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

def getListFromBD(table):
    import sqlite3
    from django.conf import settings
    conn = sqlite3.connect(settings.DATABASES["parts"]["NAME"])
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM "+table)

    # перегнать в список словарей
    dictList = sql2ListDict(cursor.execute("SELECT * FROM "+table).fetchall())

    return dictList