from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Drugs(Base):
    __tablename__ = 'drugs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    stock = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
