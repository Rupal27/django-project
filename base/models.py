from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) # its nullable 
    # participants = // only if they're commenting
    updated = models.DateTimeField(auto_now=True) 
    # its gonna record the ts on its own for above field
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Office(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    roomNumber = models.IntegerField(max_length=100)    
    description = models.TextField(null=True,blank=True) # its nullable 
    # participants = // only if they're commenting
    updated = models.DateTimeField(auto_now=True) 
    # its gonna record the ts on its own for above field
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
    


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    room = models.ForeignKey(Room,on_delete=models.CASCADE)         
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    # its gonna record the ts on its own for above field
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50] 