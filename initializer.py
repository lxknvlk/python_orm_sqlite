import sqlite3, sys, inspect, os, const, manager

from objects.user import User
from objects.location import Location

def init():
    print "creating database with next structure:"
    classes = []

    print const.DBNAME

    conn = sqlite3.connect(const.DBNAME)
    c = conn.cursor()

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            classes.append(obj)
            query = ""
            print "class: " + str(obj)
            print "table: " + str(obj.table)
            query += "create table if not exists " + str(obj.table) + "("

            fields = manager.getClassFields(obj)

            for x in range(0, len(fields)):
                field = fields[x]
                print "         " + field
                query += field + " "
                f = getattr(obj, field)

                if type(f) is str:
                    query += "VARCHAR"
                elif type(f) is int:
                    query += "INTEGER"

                if x == 0:
                    query += " PRIMARY KEY"

                if x != len(fields) - 1:
                    query += ", "

            query += ")"

            c.execute(query)
            print query

    conn.commit()
    conn.close()

    return

def drop():
    if os.path.isfile(const.DBNAME):
        os.remove(const.DBNAME)
    return

def remake():
    drop()
    init()
    return
