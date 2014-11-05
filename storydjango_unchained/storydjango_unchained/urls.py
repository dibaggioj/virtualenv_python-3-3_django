from django.conf.urls import patterns, include, url
from django.contrib import admin #for Admin app (for accessing a CRUD interface)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project_unchained.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #for Admin app (for accessing a CRUD interface)
    url(r'^$', 'story.views.home', name='home'), 
    # url(
    	# regex for start here and end here with not in-between meaning that I didn't get a path,
    	# import path to a django view,
    	# url name
    	# )
)
