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

def topic(request, topic_id):
    """Выводит одну из тем и все её записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_add')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'site/topic.html', context)
