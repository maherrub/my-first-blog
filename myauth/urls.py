from django.conf.urls import url, include
from . import views 

app_name = 'myauth'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]