"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns=[
url(r'^login/$',views.loginit,name='login'),
url(r'^logout/$',views.logout_view,name='logout'),
url(r'^register/$',views.register,name='register'),]
