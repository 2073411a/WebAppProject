from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
		return self.user.username

class Leaderboard(models.Model):
    seed = models.CharField(max_length=128, unique=True)
    plays = models.IntegerField(default = 0)
    challanges = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.seed

#class Challange(models.Model):
    #challanger = models.OneToOneField(User)
    #challanged = models.OneToOneField(User)
    #seed = models.CharField(max_length=128, unique=True)
    #score = models.IntegerField(default = 0)
    #def __unicode__(self):
    #    return self.seed + self.challanger.username + self.challanged.username
