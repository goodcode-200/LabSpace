from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^publish/$',views.publish),
    url(r'^search/$',views.search),
    url(r'^tag_info/(?P<tag_pk>.*?)/$',views.tagInfo),
    url(r'^detail/(?P<title_pk>.*?)/$',views.detail),
]