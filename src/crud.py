from sqlalchemy import select, update, insert


def isLocked(session):
    result = session['Locked']
    return result is not None and result == "Yes"


def isLicenseExpired(session, date):
    result = session['ExpirationDate']
    if result <= date and result == '':
        updateData(session=session, key="Locked", value="Yes")
    return result is not None and result < date


def isSerialNoSame(session, serialNo):
    result = session['SerialNumber']
    return result is not None and result == serialNo


def readLisences(path):
    try:
        data = []
        with open(path, 'r') as f:
            data = f.readlines()
            f.close()
        return data
    except:
        return []


def removeLisence(path, lisences, my_lisence):
    with open(path, 'w') as f:
        for lisence in lisences:
            if lisence[:-1] != my_lisence:
                f.write(lisence)
        f.close()


def matchLisence(lisences, my_lisence):
    if lisences != []:
        for lisence in lisences:
            if lisence[:-1] == my_lisence:
                return True
        return False
    else:
        print("Lisences File Not Found")
        exit()


def updateData(session, key, value):
    session[key] = value
    return True


def insertData(session, key, value):
    session[key] = value
    return True
