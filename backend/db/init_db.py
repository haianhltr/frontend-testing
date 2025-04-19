# db/init_db.py
import time
from sqlalchemy.exc import OperationalError

def init_db():
    from domains.decom.models import Base
    from db.session import engine

    for _ in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database initialized.")
            return
        except OperationalError as e:
            print("⏳ Waiting for DB to be ready...")
            time.sleep(2)
    raise Exception("❌ Could not connect to database after 10 tries.")
