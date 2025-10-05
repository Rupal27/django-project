from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


rooms = [{'id':1, 'name':'Room 1'},
        {'id':2, 'name':'Room 2'},
        {'id':3, 'name':'Room 3'},
        ]



def home(request):
    print(Room.objects.all())
    print('hello')
    return render(request,'home.html',{'rooms':Room.objects.all()})

def office(request):
    print('hello')
    return render(request,'office.html')
