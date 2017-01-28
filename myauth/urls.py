from django.conf.urls import url, include
from . import views 

app_name = 'myauth'

urlpatterns = [
   
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
]