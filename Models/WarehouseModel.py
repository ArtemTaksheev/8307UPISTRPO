from .BaseModel import *


class Warehouse(Base):
    __tablename__ = 'Warehouse'
    PartID = Column(Integer, primary_key=True, autoincrement=True)
    PartName = Column(String(100), nullable=False)
    PartAmount = Column(Integer, nullable=False)
    part_service_id = Column(Integer, ForeignKey('PriceList.PartServiceID'), nullable=False)
    service = relationship('PriceList', backref='warehouse')