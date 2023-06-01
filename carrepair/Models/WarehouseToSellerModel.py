from .BaseModel import *


class WarehouseToSeller(Base):
    __tablename__ = 'WarehouseToSeller'
    WarehousePartID = Column(Integer, ForeignKey('Warehouse.PartID'), primary_key=True)
    SellerID = Column(Integer, ForeignKey('Sellers.SellerID'), primary_key=True)
    seller = relationship('Sellers', backref='warehouse_to_seller')
    warehouse = relationship('Warehouse', backref='warehouse_to_seller')