from Pages.src.crud import readLisences, isLocked, matchLisence, removeLisence, updateData, insertData
from Pages.src.core.config import conf
from Pages.src.core.db import session, settings_table
import os
from Pages.src.similarity import runner

BASE_PATH = os.path.abspath(os.getcwd())



if __name__ == "__main__":
    # print(getProcessor_batch_serial_info("p"))


    if not isLocked(session=session, table=settings_table):
        runner(option=1, case_image='/home/anonymous/Documents/FaceAI_GUI_PyQT/models/1.jpg', target_images=['/home/anonymous/Documents/FaceAI_GUI_PyQT/models/3.jpg', '/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg'])
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
