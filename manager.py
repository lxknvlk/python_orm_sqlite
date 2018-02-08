import sqlite3, const, datetime, utils

def update(object):
    object.updated = utils.getCurrentDateAsString()

    result = "ok"
    query = "update " + object.table + " set "
    fields = []

    for x in range(0, len(object.fields)):
        field = object.fields[x]
        fieldname = field.split(" ", 1)[0]

        if fieldname == "created":
            continue

        query += fieldname + " = "
        query += "'" + str(getattr(object, fieldname)) + "'"
        fields.append(fieldname)
        if x != len(object.fields) - 1:
            query += ", "

    idfield = object.fields[0]
    id = getattr(object, idfield)

    query += " where " + idfield + " = '" + id + "'"

    print query

    conn = sqlite3.connect(const.DBNAME)
    c = conn.cursor()

    try:
        c.execute(query)
    except Exception as e:
        print e
        result = "error"
    finally:
        conn.commit()
        conn.close()

    return result

def create(object):
    object.created = utils.getCurrentDateAsString()
    object.updated = utils.getCurrentDateAsString()

    result = "ok"
    query = "insert into " + object.table + " ("

    for x in range(0, len(object.fields)):
        fieldname = object.fields[x]
        query += fieldname
        if x != len(object.fields) - 1:
            query += ", "

    query += ") values ("

    for x in range(0, len(object.fields)):
        field = object.fields[x]
        if type(getattr(object, field)) is str:
            query += "'"
        query += str(getattr(object, field))
        if type(getattr(object, field)) is str:
            query += "'"
        if x != len(object.fields) - 1:
            query += ", "

    query += ")"

    print query

    conn = sqlite3.connect(const.DBNAME)
    c = conn.cursor()

    try:
        c.execute(query)
    except Exception as e:
        if 'UNIQUE constraint' in e.message:
            result = "already exists"
        else :
            print e
            result = "error"
    finally:
        conn.commit()
        conn.close()

    return result

def fetch(object):
    fields = object.fields
    idfield = object.fields[0]
    id = getattr(object, idfield)

    conn = sqlite3.connect(const.DBNAME)
    c = conn.cursor()

    c.execute("SELECT * FROM " + object.table + " WHERE " + idfield + " = '" + id + "'")
    r = c.fetchone()

    for x in range(0, len(fields)):
        name = fields[x].split(" ", 1)[0]
        value = r[x]
        setattr(object, name, value)

    conn.commit()
    conn.close()

    return object
