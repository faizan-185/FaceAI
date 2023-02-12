from sqlalchemy import select
from core.db import session, settings_table
from core.config import conf


def is_locked(session, table):
  query = select(table).where(table.columns[0] == "Locked")
  result = session.execute(query).first()
  return result is not None and result[1] == "Yes"


print(is_locked(session=session, table=settings_table))
