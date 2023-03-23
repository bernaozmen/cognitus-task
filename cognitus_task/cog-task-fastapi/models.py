from sqlalchemy import Date, Column, Integer, String
from database import Base


class Record(Base):
    __tablename__ = "cognitustask_data"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    label = Column(String)

