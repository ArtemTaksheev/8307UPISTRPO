from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from Models.ClientsOrdersModel import ClientsOrders
from Models.EmployeesModel import Employees


def SQLRequest():
    # Создание подключения к базе данных
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/carService_db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Запрос таблички с пользователями и их заказами
    query = session.query(Employees.EmployeeFIO, ClientsOrders.OrderCode, ClientsOrders.OrderDefinition).\
        join(ClientsOrders)
    result = query.all()
    return result

