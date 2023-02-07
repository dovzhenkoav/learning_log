from django.contrib import admin
from models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')


admin.site.register(Topic)
