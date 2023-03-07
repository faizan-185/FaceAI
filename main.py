from src.crud import readLisences, isLocked, matchLisence, removeLisence, updateData, insertData, isSerialNoSame, isLicenseExpired
from src.core.db import session, settings_table
from src.similarity import runner
import platform, subprocess, re, os
from src.AES256 import AES256
from src.core.config import conf
import ntplib as ntp
from datetime import date
from dateutil.relativedelta import relativedelta
import socket
import struct
import time


def getProcessor_batch_serial_info(cmd):
    if platform.system() == "Windows":
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        if completed.stdout != "":
            info = completed.stdout
            info = info.strip()
            info = info.decode('utf-8')
            infoObj = dict(item.split(":") for item in re.sub('\s+', '', re.sub('\n', ';', info)).split(";"))
            return infoObj


def getNtpTime():
    addr = '0.pool.ntp.org'
    REF_TIME_1970 = 2208988800  # Reference time
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970
    return time.ctime(t), t


def encryptFile(aes=AES256(), filePath=str):
    is_file = os.path.isfile(filePath)
    is_dir = os.path.isdir(filePath)

    if not is_file and not is_dir:
        raise ValueError("File or directory doesn't exist.")

    password = aes.read_password(conf.PASS_PATH)
    if not password:
        raise ValueError("Password File is not Correct")
    if is_file:
        aes.encrypt(password, filePath)
        return True
    elif is_dir:
        for (dirpath, dirname, filenames) in os.walk(filePath):  # Files of each subdirectory
            for filename in filenames:
                filename = os.path.join(dirpath, filename)
                aes.encrypt(password, filename)
        return True
    return False


def getExpirationDate(today):
    if conf.LICENSE_TYPE is "Year":
        return date(today) + relativedelta(years=+conf.LICENSE_DURATION)
    elif conf.LICENSE_TYPE is "Month":
        return date(today) + relativedelta(months=conf.LICENSE_DURATION)
    else:
        return date(today) + relativedelta(days=conf.LICENSE_DURATION)


def dycriptFile(aes=AES256(), filePath=str):
    is_file = os.path.isfile(filePath)
    is_dir = os.path.isdir(filePath)

    if not is_file and not is_dir:
        raise ValueError("File or directory doesn't exist.")

    password = aes.read_password(conf.PASS_PATH)
    if not password:
        raise ValueError("Password File is not Correct")
    if is_file:
        return aes.decrypt(password, filePath)
    elif is_dir:
        for (dirpath, dirname, filenames) in os.walk(filePath):  # Files of each subdirectory
            for filename in filenames:
                filename = os.path.join(dirpath, filename)
                aes.decrypt(password, filename)
        return True
    return False


if __name__ == "__main__":
    ntpDateTime = getNtpTime()
    aes = AES256()
    if not os.path.exists(conf.ENCRYPTED_LICENSE_PATH) and os.path.exists(conf.LISENCES_PATH):
        conf.IS_ENCRYPTED = encryptFile(aes=AES256, filePath=conf.LISENCES_PATH)
    else:
        print("Licenses File Missing or Manipulated Exiting Application!")
    if not conf.IS_ENCRYPTED:
        print("Retrying the Encryption...")
        conf.IS_ENCRYPTED = encryptFile(aes=AES256, filePath=conf.LISENCES_PATH)

    if conf.IS_ENCRYPTED:
        processor_dict = getProcessor_batch_serial_info("get-wmiobject win32_baseboard")
        processor_serial_no = 0 if processor_dict['SerialNumber'] == '' else int(processor_dict['SerialNumber'])

        if isLocked(session=session, table=settings_table) and isSerialNoSame(session=session, table=settings_table,
                                                                              serialNo=processor_serial_no) and isLicenseExpired(ntpDateTime):
            runner()
        else:
            license_key = input("Enter License Key: ")
            licenses = dycriptFile(aes=aes, filePath=conf.ENCRYPTED_LICENSE_PATH)
            result = matchLisence(lisences=licenses, my_lisence=license_key)
            if result:
                removeLisence(path=conf.LISENCES_PATH, lisences=licenses, my_lisence="abcd")
                updateData(session=session, table=settings_table, key="Locked", value="No")
                insertData(session=session, table=settings_table, data=("validity time", "one year"))
                insertData(session=session, table=settings_table, data=("SerialNumber", processor_serial_no))
                insertData(session=session, table=settings_table, data=("ExpirationDate", getExpirationDate(today=ntpDateTime)))
            else:
                print("Incorrect License Key or Expired License key or Not same SerialNo")
    else:
        print("Unable to Encrypt the Data so Exiting the Application!")
    # dycriptFile(aes=aes,filePath="E:/Data/Pycharm Projects/FaceAI/FaceAI/Lisences_c.txt.aes")
