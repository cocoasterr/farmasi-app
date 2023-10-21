from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Drugs(Base):
    __tablename__ = 'drugs'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    stock = Column(Integer)
    receipt = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
