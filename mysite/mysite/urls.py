from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^polls/', include('polls.urls', namespace='polls')),  # namespace each app in a project
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.

# When somebody requests a page from your Web site - say, /polls/34/, Django will load the mysite.urls Python module
# because it is pointed to by the ROOT_URLCONF setting.
# It finds the variable named urlpatterns and traverses the regular expressions in order. 
# The include() functions we are using simply reference other URLconfs. 
# Note that the regular expressions for the include() functions do not have a $ (end-of-string match character) but
# rather a trailing slash.
# Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the
# remaining string to the included URLconf for further processing.

# If a user goes to /polls/34/ in this system:
# Django will find the match at "^polls/""
# Then, Django will strip off the matching text polls/ and send the remaining text - 34/ - to the polls.urls
# URLconf for further processing which matches r"^(?P<question_id>\d+)/$"" resulting in a call to the detail() view
# like so:
# detail(request=<HttpRequest object>, question_id="34")