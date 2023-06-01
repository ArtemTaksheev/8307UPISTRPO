from .BaseModel import *


class Payments(Base):
    __tableName__ = 'Payments'
    PaymentOrderCode = Column(Integer, ForeignKey('Diagnostics.OrderCode'), primary_key=True)
    PaymentCarRegNum = Column(String(10), nullable=False)
    PaymentPriceToPay = Column(Integer, nullable=False)
    PaymentStatus = Column(Boolean, nullable=False)
    PaymentDiscount = Column(Integer)
    order = relationship('Diagnostics', backref='payments')