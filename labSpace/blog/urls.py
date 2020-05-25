from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_blog/(?P<space>.*?)$',views.create_blog),
    url(r'^create_blog_deal/(?P<space>.*?)$',views.create_blog_deal),
]