from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
# make database models

# topic can have multiple rooms but room can have only one topic
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name="participants",blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    # default user model
    # user can have many mesages (one to many relationship)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # on delete = models.SET_NULL mean stay in db
    # on_delete = models.CASCADE maens we delete every message in room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self) -> str:
        return self.body[0:50]