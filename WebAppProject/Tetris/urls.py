from django.conf.urls import patterns,url,static
from Tetris import views
from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = patterns('',
					   url(r'^play$',views.play,name='play'),
					   url(r'^$',views.index,name='index'),
                       url(r'^game/(?P<seed>[\w\-]+)/(?P<u>[\w\-]+)/$', views.challenge),
                       url(r'^game/(?P<seed>[\w\-]+)/$', views.game),
					   url(r'^play/(?P<seed>[\w\-]+)/(?P<u>[\w\-]+)/$', views.challenge),
                       url(r'^play/(?P<seed>[\w\-]+)/$', views.game, name='play'),
                       url(r'^leaderboard/(?P<seed>[\w\-]+)/$', views.leaderboard),
                       url(r'^userpage/$', views.userpage,name="userpage"),
                       url(r'^#about/$', views.about,name='about'),
					   url(r'^leaderboard$', views.leaderboard,name='leaderboard'),
                       url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
					   url(r'^score/(?P<seed>[\w\-]+)/(?P<score>[\w\-]+)/$', views.score),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         "serve",
        {'document_root': settings.MEDIA_ROOT}), )
