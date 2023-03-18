import os
from .config import conf
from src.AES256 import AES256


def check_db(path):
    try:
        return os.path.isfile(path=path)
    except:
        return False


def create_get_session():
    if check_db(path=conf.DB_PATH) and not check_db(conf.ENCRYPTED_DB_PATH):
        aes = AES256()
        password = aes.read_password(conf.PASS_PATH)
        conf.IS_DATABASE_ENCRYPTED = aes.encrypt(passwd=password, input_file_path=conf.DB_PATH)
        return eval(aes.decrypt(passwd=password, input_file_path=conf.ENCRYPTED_DB_PATH))
    elif check_db(path=conf.ENCRYPTED_DB_PATH):
        aes = AES256()
        password = aes.read_password(conf.PASS_PATH)
        return eval(aes.decrypt(passwd=password, input_file_path=conf.ENCRYPTED_DB_PATH))
    else:
        return None


conn = create_get_session()
if conn is None:
    print("Database is missing. Please insert database.")
    exit()
