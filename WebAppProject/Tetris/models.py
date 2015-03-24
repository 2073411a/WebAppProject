from django.db import models, connection
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
    likes = models.IntegerField(default = 0)
    creation_date = models.DateTimeField(auto_now_add = True, editable=False)
    class Meta:
      get_latest_by = 'creation_date'
    def __unicode__(self):
        return self.seed
    def addPlay(self):
        self.plays += 1
    def addChallenge(self):
        self.challanges += 1
    def addLike(self):
        self.likes += 1

class Score(models.Model):
    leaderboard = models.ForeignKey(Leaderboard, unique = False)
    user = models.ForeignKey(User, unique = False)
    score = models.IntegerField(default = 0)
    #def __unicode__(self):
	#	return self.user.user.username + '_' + self.leaderboard.seed
