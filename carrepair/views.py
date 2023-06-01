from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
#from .SQLRequestor import *
from .Models import PaymentsModel

import datetime
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


context = {}

def index(request):
    return render(request, "index.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    context['price'] = "0"
    context['priceorder'] = "0"
    context['supplier1'] = 'ООО "Колёса"'
    context['partnameorder'] = ""
    context['ordernumorder'] = ""
    context['dateorder'] = ""
    context['base_info'] = ""
    context['registered'] = ""
    context['namepay'] = ""
    context['comment'] = ""
    name = request.POST.get("name", "Undefined")
    password = request.POST.get("password", 1)
    #result = SQLRequest()
    #for row in result:
    #    logger.warning("Пользователь:", row[0])
    #    logger.warning("Заказ №:", row[1])
    #    logger.warning("Описание заказа:", row[2])
    #    logger.warning("-----")

    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(name) + ' Pass:' + str(password))
    return redirect('index')

def postregistration(request):
    # получаем из данных запроса POST отправленные через форму данные
    master = request.POST.get("master", "Undefined")
    master = master[master.find('selected') + 10:]
    master = master[:master.find('<')]
    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(master))
    context['registered'] = "Зарегистрировано!"
    return redirect('registration')

def renewpay(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("clientname", "Undefined")
    context['price'] = "120"
    context['comment'] = "Information here"
    context['namepay'] = name
    logger.warning('Got info about user at ' + str(name))
    return redirect('pay')

def reneworder(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("clientname", "Undefined")
    dateorder = request.POST.get("trip-start")
    partnameorder = request.POST.get("ordername")
    ordernumorder = request.POST.get("ordernum")
    priceorder = 120
    context['priceorder'] = priceorder
    context['partnameorder'] = partnameorder
    context['ordernumorder'] = ordernumorder
    context['workorder'] = ""
    context['dateorder'] = dateorder
    context['supplier1'] = 'ООО "Колёса"'
    logger.warning('Got info about user at ' + str(name))
    return redirect('order')

def renewdb(request):
    # получаем из данных запроса POST отправленные через форму данные
    if 'output' in request.POST:
        base_info = 'Name and stuff'
        context['base_info'] = base_info
        return redirect('access')
    elif 'clear' in request.POST:
        base_info = ''
        context['base_info'] = base_info
        return redirect('access')


def index(request):
    return render(request, "index.html")

def registration(request):
    name_master1 = 'Tom'
    context['name_master1'] = name_master1
    return render(request, "registration.html", context)


def order(request):
    return render(request, "order.html", context)

def pay(request):
    return render(request, "pay.html", context)

def access(request):
    return render(request, "access-to-bd.html", context)

def login(request):
    return render(request, "login.html")