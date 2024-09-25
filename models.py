
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class PopularityData(Base):
    __tablename__ = 'popularity_data'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    metric1 = Column(Integer)
    metric2 = Column(Integer)
    metric3 = Column(Integer)
    popularity_score = Column(Float)
