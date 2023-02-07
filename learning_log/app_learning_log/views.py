from django.shortcuts import render
from .models import Topic


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'site/index.html')

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'site/topics.html', context)
