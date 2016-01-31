from django.conf.urls import patterns, url

urlpatterns = patterns('tentagarden.views',
	url(r'^$', 'home', name='home'),
	url(r'^list/$', 'list', name='list'),
	url(r'^login/$', 'user_login', name='login'),
	url(r'^logout/$', 'user_logout', name='logout'),
)
