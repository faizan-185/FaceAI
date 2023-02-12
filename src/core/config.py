import os


class Config:
  DB_PATH: str = f"{os.getcwd()}/FaceAI"
  PICKLE_PATH: str = f"{os.getcwd()}/Lisences.pickle"

conf = Config()
