from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.sign_in, name='sign in'),
]