from django.db import models

class Users(models.Model):
	email = models.CharField(max_length=100, primary_key=True)
	password = models.CharField(max_length=1000)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)


class Problems(models.Model):
	url = models.CharField(max_length=1000, primary_key=True)
	name = models.CharField(max_length=100)
	is_solved = models.BooleanField(default=False)
	site = models.CharField(max_length=100)