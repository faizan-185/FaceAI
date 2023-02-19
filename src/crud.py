from sqlalchemy import select, update, insert


def isLocked(session, table):
  query = select(table).where(table.columns[0] == "Locked")
  result = session.execute(query).first()
  return result is not None and result[1] == "Yes"


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


def updateData(session, table, key, value):
  query = update(table).where(table.columns[0] == "Locked").values((key, value))
  session.execute(query)
  session.commit()


def insertData(session, table, data):
  query = insert(table).values(data)
  session.execute(query)
  session.commit()
