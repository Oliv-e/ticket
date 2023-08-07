from django.db import models
import datetime

# Create your models here.
class EventOrganizer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    email = models.EmailField()
    telp = models.TextField(max_length=20)
    created_at = datetime.datetime.now()
    
    def __str__(self):
        return self.name
class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    organizer = models.TextField()

    def __str__(self):
        return self.title