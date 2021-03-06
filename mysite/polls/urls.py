# from django.conf.urls import url
from django.conf.urls import patterns, include, url
from polls.controller import authController
from . import views

urlpatterns = [
    url(r'^$', views.index, name='polls'),
    url(r'^home/$', views.home, name='home'),
    url(r'^highchart/$', views.highchart, name='highchart'),
    url(r'^highchart/api/$', views.highchart_api, name='highchart_api'),
    url(r'^pages/(?P<page_name>[\w\-]+)/$', views.load_page, name='load_page'),
    url(r'^page/file_upload/$', views.file_upload, name='file_upload'),

    url(r'^demo/(?P<pk>\d+)/(?P<id>\d+)/$', views.demo, name='demo'),

    url(r'^login/$', authController.login, name='login'),
    url(r'^logout/$', authController.logout, name='logout'),
    url(r'^login/pages/$', authController.load_login_page, name='login_page'),
]