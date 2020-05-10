from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker


class Port(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tick = models.CharField(max_length=10, unique=True)
	shares = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user.username} Profile'