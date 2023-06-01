from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from .SQLRequestor import *
from .Models import PaymentsModel

import datetime
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    password = request.POST.get("password", 1)
    result = SQLRequest()
    for row in result:
        logger.warning("Пользователь:", row[0])
        logger.warning("Заказ №:", row[1])
        logger.warning("Описание заказа:", row[2])
        logger.warning("-----")

    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(name) + ' Pass:' + str(password))
    return redirect('index')

def postregistration(request):
    # получаем из данных запроса POST отправленные через форму данные
    master = request.POST.get("master", "Undefined")
    master = master[master.find('selected') + 10:]
    master = master[:master.find('<')]
    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(master))
    return redirect('index')

def renewpay(request):
    # получаем из данных запроса POST отправленные через форму данные
    master = request.POST.get("master", "Undefined")
    master = master[master.find('selected') + 10:]
    master = master[:master.find('<')]
    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(master))
    return redirect('index')

def index(request):
    return render(request, "index.html")

def registration(request):
    context = {}
    name_master1 = 'Tom'
    context['name_master1'] = name_master1
    return render(request, "registration.html", context)


def order(request):
    return render(request, "order.html")

def pay(request):
    #payments = PaymentsModel.objects.all()
    #return render(request, "pay.html", {"payments":payments})
    return render(request, "pay.html")

def access(request):
    context = {}
    base_info = 'Name and stuff'
    context['base_info'] = base_info
    return render(request, "access-to-bd.html", context)

def login(request):
    return render(request, "login.html")