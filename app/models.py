from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    requirements = Column(JSON)

    def __repr__(self):
        return f"<Configuration(country_code={self.country_code}, requirements={self.requirements})>"
