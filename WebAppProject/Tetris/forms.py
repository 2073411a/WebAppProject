from django import forms
from django.contrib.auth.models import User
from Tetris.models import UserProfile,Leaderboard,Score

class ScoreForm(forms.ModelForm):
    user = forms.CharField(max_length = 128)
