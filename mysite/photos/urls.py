from django.conf.urls import patterns, url, static, include
from django.contrib import admin
from django.views.generic import TemplateView

from photos import views

urlpatterns = patterns('',
  url(r'^uploadfile/$', views.upload_photo, name='uploadphoto'),
  url(r'^listfiles/$', views.display_photo, name='displayphoto'),
  url(r'^afterupload/$', TemplateView.as_view(template_name='photos/afterupload.html'), name='afterupload')
)