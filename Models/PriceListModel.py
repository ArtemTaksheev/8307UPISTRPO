from .BaseModel import *


class PriceList(Base):
    __tablename__ = 'PriceList'
    PartServiceID = Column(Integer, primary_key=True, autoincrement=True)
    PartServiceName = Column(String(100), nullable=False)
    Price = Column(Integer, nullable=False)