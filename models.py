from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    rating = Column(Integer)
    comment = Column(String)
    rating = Column(Integer)
    plate_id = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))