from django.db import models

from django.contrib.auth.models import User


class Board(models.Model):
	name = models.CharField(max_length=30, unique=True) # unique=True enforce the uniqueness of the field at the database level
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.nameoar


class Topic(models.Model):
	subject = models.CharField(max_length=225)
	last_updated = models.DateTimeField(auto_now_add=True) # auto_now_add=True instruct Django to set the current date and time
	board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE) # related_name='topics' parameter will be used to create a reverse relationship
	starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
	#Django automatically creates this reverse relationship – the related_name is optional. 
	#But if we don’t set a name for it, Django will generate it with the name: (class_name)_set.
	# For example, in the Board model, the Topic instances would be available under the topic_set property.
	# Instead, we simply renamed it to topics, to make it feel more natural.


class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE) # related_name='+' instructs Django that we don’t need this reverse relationship, so it will ignore it.

