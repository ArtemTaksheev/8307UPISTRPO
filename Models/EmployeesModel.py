from BaseModel import *


class Employees(Base):
    __tablename__ = 'Employees'
    EmployeeCode = Column(Integer, primary_key=True, autoincrement=True)
    EmployeeFIO = Column(String(255), nullable=False)
    EmployeePasport = Column(String(255), nullable=False)
    EmployeePosition = Column(String(20), nullable=False)
    EmployeeDivisionCode = Column(Integer, nullable=False)
    EmployeeMedID = Column(String(255), nullable=False)