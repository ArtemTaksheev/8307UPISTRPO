from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from random import randrange

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
context['base_info1'] = ""
context['login_succ'] = ""

def index(request):
    return render(request, "index.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    password = request.POST.get("password", 1)
    #result = SQLRequest()
    #for row in result:
    #    logger.warning("Пользователь:", row[0])
    #    logger.warning("Заказ №:", row[1])
    #    logger.warning("Описание заказа:", row[2])
    #    logger.warning("-----")

    logger.warning('Got info about user at ' + str(datetime.datetime.now()) + ', Username:' + str(name) + ' Pass:' + str(password))
    if (name == "Владислав") & (password == "asd"):
        return redirect('index')
    elif (name != "Владислав"):
        context['login_succ'] = "Неверное имя пользователя!"
        return redirect('login')
    elif (password != "asd"):
        context['login_succ'] = "Неверный пароль!"
        return redirect('login')

def postregistration(request):
    # получаем из данных запроса POST отправленные через форму данные
    master = request.POST.get("master", "Undefined")
    regname = request.POST.get("name", "Undefined")
    regdate = request.POST.get("date", "Undefined")
    regtime = request.POST.get("time", "Undefined")
    diagnosis = request.POST.get("diagnosis", "off")
    repairs = request.POST.get("repairs", "off")
    master = master[master.find('selected') + 10:]
    master = master[:master.find('<')]
    context['base_info1'] += str(regname) + ', ' + str(master) + ', ' + str(regdate) + ', ' + str(regtime) + ', diagnosis:' + str(diagnosis) + ', repairs:' + str(repairs) + ";\n"
    logger.warning(str(context['base_info1']))
    context['registered'] = "Зарегистрировано!"
    return redirect('registration')

def renewpay(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("clientname", "Undefined")
    masterpay = request.POST.get("master", "Undefined")
    masterpay = masterpay[masterpay.find('selected') + 12:]
    masterpay = masterpay[:masterpay.find('<')]
    if (masterpay == "Мастер 1") & (name == "Владислав"):
        context['price'] = str(randrange(12, 100) * 10)
        context['comment'] = "Comm"
    else:
        context['price'] = "0"
        context['comment'] = "Неверная комбинация клиента и мастера!"
    context['namepay'] = name
    logger.warning('Got info about user at ' + str(masterpay))
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
        context['base_info'] = context['base_info1']
        return redirect('access')
    elif 'clear' in request.POST:
        base_info = ''
        context['base_info'] = base_info
        return redirect('access')


def index(request):
    context['price'] = "0"
    context['priceorder'] = "0"
    context['supplier1'] = 'ООО "Колёса"'
    context['partnameorder'] = ""
    context['ordernumorder'] = ""
    context['dateorder'] = ""
    context['registered'] = ""
    context['namepay'] = ""
    context['comment'] = ""
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
    return render(request, "login.html", context)