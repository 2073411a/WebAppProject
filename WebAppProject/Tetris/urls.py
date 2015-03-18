from django.conf.urls import patterns,url,static
from Tetris import views
from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = patterns('',
					   url(r'^play$',views.play,name='index'),
					   url(r'^$',views.index,name='index'),
                       url(r'^game/(?P<seed>[\w\-]+)/(?P<username>[\w\-]+)/$', views.challenge),
                       url(r'^game/(?P<seed>[\w\-]+)/$', views.game),
                       url(r'^leaderboard/(?P<seed>[\w\-]+)/$', views.leaderboard),
                       url(r'^userpage/$', views.userpage,name="userpage"),
                       url(r'^#about/$', views.about,name='about'),
                       url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         "serve",
        {'document_root': settings.MEDIA_ROOT}), )
