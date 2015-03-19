from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=1024) # I Don't know how long this should be?
    def __unicode__(self):
		return self.user.username

class Leaderboard(models.Model):
    seed = models.CharField(max_length=128, unique=True)
    plays = models.IntegerField(default = 0)
    challanges = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.seed

class Score(models.Model):
    leaderboard = models.ForeignKey(Leaderboard, unique = False)
    user = models.ForeignKey(User, unique = False)
    score = models.IntegerField(default = 0)
    #def __unicode__(self):
	#	return self.user.user.username + '_' + self.leaderboard.seed
