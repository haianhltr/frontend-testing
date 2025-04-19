from sqlalchemy import Column, String, JSON
from db.engine import Base

class Machine(Base):
    __tablename__ = "machines"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    stages = Column(JSON, nullable=False)
