import re
from dataclasses import dataclass
from sqlalchemy.orm import validates
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

    def __init__(self, **kwargs) -> None:
        self.name = kwargs['name'].title()
        self.email = kwargs['email'].lower()
        self.phone = kwargs['phone']
        
    @validates("phone")
    def validate_phone(self, _, phone_to_be_tested):
        phone_is_valid = re.fullmatch("^\([1-9]{2}\)[9]{0,1}[0-9]{1}[0-9]{3}\-[0-9]{4}$", phone_to_be_tested)
        
        if phone_is_valid:
            return phone_to_be_tested
        else:
            raise ValueError("Invalid phone format!")
