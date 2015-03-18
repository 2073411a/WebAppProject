from django.conf.urls import include, url, static, patterns
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/Tetris/edit_profile/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Tetris/', include('Tetris.urls')),
    url(r'^tetris/', include('Tetris.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$',include('Tetris.urls')),
	
)
