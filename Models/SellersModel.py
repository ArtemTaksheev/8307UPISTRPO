from BaseModel import *


class Sellers(Base):
    __tableName__ = 'Sellers'
    SellerID = Column(Integer, primary_key=True, autoincrement=True)
    SellerName = Column(String(100), nullable=False)
    SellerContactName = Column(String(100), nullable=False)
    SellersPhone = Column(String(100), nullable=False)