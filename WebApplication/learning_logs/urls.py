from django.conf.urls import url
from . import  views

# urls for learning logs
urlpatterns = [
    #Main page
    url(r'^$', views.index, name='index'),
    #All topics page
    url(r'^topics/$', views.topics, name='topics')

]