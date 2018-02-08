import datetime

def getCurrentDateAsString():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print string
    #
    # datetime_object = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    # print datetime_object