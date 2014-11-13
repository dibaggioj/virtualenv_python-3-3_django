#from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'), # ex: /polls/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), # ex: /polls/5/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'), # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'), # ex: /polls/5/vote/
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
