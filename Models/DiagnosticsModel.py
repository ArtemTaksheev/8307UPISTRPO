from .BaseModel import *


class Diagnostics(Base):
    __tableName__ = 'Diagnostics'
    OrderCode = Column(Integer, primary_key=True, autoincrement=True)
    DiagnosticCarNumber = Column(String(10), nullable=False)
    DiagnosticResult = Column(Text, nullable=False)
    order = relationship('ClientsOrders', backref='diagnostics')
    OrderCode_fk = Column(Integer, ForeignKey('ClientsOrders.OrderCode'), nullable=False)