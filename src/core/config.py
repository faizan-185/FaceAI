import os


class Config:
    DB_PATH: str = f"{os.getcwd()}/FaceAI.json"
    LISENCES_PATH: str = f"{os.getcwd()}/Lisences.txt"
    PASS_PATH: str = f"{os.getcwd()}/password.txt"
    ENCRYPTED_LICENSE_PATH = str = f"{os.getcwd()}/Lisences.txt.aes"
    ENCRYPTED_DB_PATH = str = f"{os.getcwd()}/FaceAI.json.aes"
    IS_LICENSE_ENCRYPTED = False
    IS_DATABASE_ENCRYPTED = False
    IS_DB_CREATED = False
    LICENSE_TYPE = "YEAR"
    LICENSE_DURATION = 1


conf = Config()
