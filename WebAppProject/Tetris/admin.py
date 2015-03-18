from django.contrib import admin
from models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio','picture')

class LeaderAdmin(admin.ModelAdmin):
    list_display = ('seed',)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('score',)

admin.site.register(Score, ScoreAdmin)
admin.site.register(Leaderboard,LeaderAdmin)
admin.site.register(UserProfile,ProfileAdmin)
