from django.conf.urls import patterns, url
from views import home

urlpatterns = patterns('',
	url(r'^home/$', home, name="home"),
	url(r'^home/(\w+)$', home, name="home")
)