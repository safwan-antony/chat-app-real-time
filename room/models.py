from django.db import models
from a_users.models import User
# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #description = models.TextField()
    slug = models.SlugField(unique=True , null=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User , related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_apdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:30]