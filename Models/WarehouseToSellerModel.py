from BaseModel import *


class WarehouseToSeller(Base):
    __tablename__ = 'WarehouseToSeller'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    WarehousePartID = Column(Integer, ForeignKey('Warehouse.PartID'), nullable=False)
    SellerID = Column(Integer, ForeignKey('Sellers.SellerID'), nullable=False)
    seller = relationship('Sellers', backref='warehouse_to_seller')
    warehouse = relationship('Warehouse', backref='warehouse_to_seller')