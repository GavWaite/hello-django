from django.db import models
from django.contrib.auth.models import User

# This is where we define our data model which will be stored in the database
# Note that we use the built in model for User
# Also worth noting is the fields are all subclasses of django.db.models.Field
# Lots of choices here

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True) # Note the unique optional parameter
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True) # Note the auto_now_add to set to time of object creation
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT) # the related_name refers to the automatic inverse relationship
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.PROTECT) # the + signifies we do not need an inverse