from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls,name="defaultpage"),
    path('', views.home, name="homepage"),
    path('office/', views.office, name="office"),
    
]