from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MainPosition(models.Model):
	slug = models.CharField(max_length=10)
	name = models.CharField(max_length=50)

class Player(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	position = models.ForeignKey(MainPosition)

class PositionStat(models.Model):
	count = models.IntegerField(default=0)
	position = models.ForeignKey(MainPosition)