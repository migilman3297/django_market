from django.db import models
from django.contrib.auth.models import User


# class Stocks(models.Model):
# 	user = models.OneToOneField(User, default='0', on_delete=models.CASCADE)
# 	stocks = models.CharField(max_length=10)
# 	shares = models.IntegerField(blank=True, null=True)
	
# 	def __str__(self):
# 		return f'{self.user.username} Stocks'


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tick = models.CharField(max_length=10)
	shares = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user.username} Profile'


class Portfolio(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tick = models.CharField(max_length=10)
	shares = models.IntegerField(default=0)


	def __str__(self):
		ret = self.user.username + ', ' + self.tick + ', ' + self.shares
		return ret


# Create your models here.
