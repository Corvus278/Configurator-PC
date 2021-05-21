import sqlite3
from django.conf import settings


def cortage2dict(cursor, cortage):
    argNames = [description[0] for description in cursor.description]
    return {argNames[i]: cortage[i] for i in range(len(argNames))}


def getListFromTable(table):
    dbName = settings.DATABASES["parts"]["NAME"]
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM "+table)

    # перегнать в список словарей
    argNames = [description[0] for description in cursor.description]
    ansList = cursor.execute("SELECT * FROM "+table).fetchall()
    dictList = [{argNames[i]: ans1[i] for i in range(len(argNames))} for ans1 in ansList]
    conn.close()
    return dictList


def getFromTable(id, table):
    conn = sqlite3.connect(settings.DATABASES["parts"]["NAME"])
    cursor = conn.cursor()
    ansCortage = cursor.execute("SELECT * FROM "+table+" WHERE id = ?", (id,)).fetchone()
    ansDict = cortage2dict(cursor, ansCortage)
    conn.close()
    return ansDict