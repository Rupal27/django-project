from django.contrib import admin
from .models import Room,Office,Message, Topic
# Register your models here.

admin.site.register(Room)
admin.site.register(Office)
admin.site.register(Message)
admin.site.register(Topic)

