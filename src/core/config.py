import os


class Config:
  DB_PATH: str = f"{os.getcwd()}/FaceAI"
  LISENCES_PATH: str = f"{os.getcwd()}/Lisences.txt"

conf = Config()
