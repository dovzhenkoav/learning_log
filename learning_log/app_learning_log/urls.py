from django.urls import path
from .views import index, topics


urlpatterns = [
    path('', index, name='index'),
    path('topics/', topics, name='topics'),

]
