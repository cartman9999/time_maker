from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	profile_pic = models.CharField(max_length=200, null=True, blank=True)
    
	def __str__(self):
		return self.name

class Tactic(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
    

class Highlight(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	start = models.DateTimeField(auto_now_add=False, null=True)
	end = models.DateTimeField(auto_now_add=False, null=True)
	completed = models.BooleanField(default=False)
	laser = models.CharField(max_length=200, null=True)
	energize = models.CharField(max_length=200, null=True)
	tactic = models.ManyToManyField(Tactic)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
 
	def __str__(self):
		return self.name