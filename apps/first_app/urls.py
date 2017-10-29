from django.conf.urls import url
from django.contrib import admin
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register$',views.register, name='create'),
    url(r'login$',views.login, name='login'),
    url(r'success$', views.success, name='success'),
    url(r'^dash$', views.dash, name='dash'),
    url(r'^first_app/(?P<id>\d+)/profile$', views.profile, name='profile'),
    url(r'^first_app/(?P<id>\d+)/addedfriend$', views.addedfriend, name='addedfriend'),
    url(r'^first_app/(?P<id>\d+)/removedfriend$', views.removedfriend, name='removedfriend'),
]