from django.db import models

class Users(models.Model):
	email = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=1000)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	handle = models.CharField(max_length=100, primary_key=True)

class Problems(models.Model):
	url = models.CharField(max_length=1000, primary_key=True)
	name = models.CharField(max_length=100)
	is_solved = models.BooleanField(default=False)
	site = models.CharField(max_length=100)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)