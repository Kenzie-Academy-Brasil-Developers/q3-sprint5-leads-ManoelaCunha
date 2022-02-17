from dataclasses import dataclass
from app.configs.database import db
from datetime import datetime as dt
from sqlalchemy import String, Column, DateTime, Integer

@dataclass
class LeadsModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "leads_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, default=dt.now())
    last_visit = Column(DateTime, default=dt.now())
    visits = Column(Integer, default=1)
