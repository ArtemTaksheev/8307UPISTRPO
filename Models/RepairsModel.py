from .BaseModel import *


class Repairs(Base):
    __tablename__ = 'Repairs'
    RepairOrderCode = Column(Integer, ForeignKey('Diagnostics.OrderCode'), primary_key=True)
    RepairCarNumber = Column(String(10), nullable=False)
    DiagnosticIncluded = Column(Boolean, nullable=False)
    DiagnosticResult = Column(Text, nullable=False)
    RepairResult = Column(Text, nullable=False)