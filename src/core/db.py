import os
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from core.config import conf


def check_db(path):
  try:
    return os.path.isfile(path=path)
  except:
    return False


def create_session():
  if check_db(path=conf.DB_PATH):
    engine = create_engine(f"sqlite:///{conf.DB_PATH}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return [engine, session]
  else:
    return None


conn = create_session()
if conn is None:
  print("Database is missing. Please insert database.")
  exit()

engine, session = conn

metadata = MetaData()

settings_table = Table("settings", metadata, autoload_with=engine, extend_existing=True)
