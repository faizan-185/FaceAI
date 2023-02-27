from src.crud import readLisences, isLocked, matchLisence, removeLisence, updateData, insertData
from src.core.config import conf
from src.core.db import session, settings_table
from src.similarity import runner

if __name__ == "__main__":
    if not isLocked(session=session, table=settings_table):
        runner()
    else:
        license_key = input("Enter License Key: ")
        licenses = readLisences(conf.LISENCES_PATH)
        result = matchLisence(lisences=licenses, my_lisence=license_key)
        if result:
            removeLisence(path=conf.LISENCES_PATH, lisences=licenses, my_lisence="abcd")
            updateData(session=session, table=settings_table, key="Locked", value="No")
            insertData(session=session, table=settings_table, data=("validity time", "one year"))

        else:
            print("Incorrect License Key")
