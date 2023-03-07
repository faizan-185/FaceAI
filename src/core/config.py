import os


class Config:
    DB_PATH: str = f"{os.getcwd()}/FaceAI"
    LISENCES_PATH: str = f"{os.getcwd()}/Lisences.txt"
    PASS_PATH: str = f"{os.getcwd()}/password.txt"
    ENCRYPTED_LICENSE_PATH = str = f"{os.getcwd()}/Lisences.txt.aes"
    IS_ENCRYPTED = False
    LICENSE_TYPE = "YEAR"
    LICENSE_DURATION = 1


conf = Config()
