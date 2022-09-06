from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница Yatube')


# Страница со списком групп
def group_list(request):
    return HttpResponse('Список групп')


# Страница с постами отфильтрованными по группам
def group_posts(request, slug):
    return HttpResponse('ПОСТ - это посты отфильтрованные по группам')
