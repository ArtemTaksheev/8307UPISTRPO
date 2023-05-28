from django.shortcuts import render
from django.http import HttpResponse, request

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
    logger.warning('Got info at ' + str(datetime.datetime.now()) + ' hours!, Name:' + str(name) + ' Pass:' + str(password))
    return HttpResponse(f"<h2>Name: {name}  Pass: {password}</h2>")

def index(request):
    return render(request, "index.html")


def registration(request):
    return render(request, "registration.html")


def order(request):
    return render(request, "order.html")

def pay(request):
    return render(request, "pay.html")

def access(request):
    user ={"name" : "shvn"}
    return render(request, "access-to-bd.html")

def login(request):
    return render(request, "login.html")