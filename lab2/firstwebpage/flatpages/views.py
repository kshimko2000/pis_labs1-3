from django.http import HttpResponse
from django.shortcuts import render
from django import template


# Первая функция - для демонстрации простого ответа
def home(request):
    return render(request, "templates/static_handler.html")


# Функции для выполнения заданий
def home_text(request):
    """Возвращает простой текст без указания типа контента"""
    return HttpResponse("Привет, Мир!")


def hello(request):
    """Обработчик для адреса /hello/"""
    return HttpResponse("Привет, Мир!", content_type="text/plain")
