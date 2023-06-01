from .BaseModel import *


class FinishedJobs(Base):
    __tableName__ = 'FinishedJobs'
    FinishedJobOrderCode = Column(Integer, ForeignKey('Diagnostics.OrderCode'), primary_key=True)
    FinishedJobServiceCode = Column(Integer, ForeignKey('PriceList.PartServiceID'), primary_key=True)
    FinishedJobID = Column(Integer, nullable=False)
    FinishedJobCost = Column(Integer, nullable=False)