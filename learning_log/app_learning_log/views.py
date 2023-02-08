from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


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


def new_topic(request):
    """Страница создания топиков"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')
    context = {'form': form}
    return render(request, 'site/new_topic.html', context)


def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'site/new_entry.html', context)

