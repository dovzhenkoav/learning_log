from django.urls import path
from .views import index, topics, topic, new_topic, new_entry


urlpatterns = [
    path('', index, name='index'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),

]
