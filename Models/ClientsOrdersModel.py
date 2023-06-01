from .BaseModel import *


class ClientsOrders(Base):
    __tableName__ = 'ClientsOrders'
    OrderCode = Column(Integer, primary_key=True, autoincrement=True)
    ClientCode = Column(Integer, nullable=False)
    EmployeeCode = Column(Integer, ForeignKey('Employees.EmployeeCode'), nullable=False)
    ClientFIO = Column(String(255), nullable=False)
    OrderCreated = Column(Date, nullable=False)
    OrderDefinition = Column(Text, nullable=False)
    OrderStatus = Column(String(10), nullable=False)
    RegistryNumber = Column(String(10), nullable=False)
    employee = relationship('Employees', backref='clients_orders')
