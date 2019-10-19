from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^search/',views.search,name='search'),
    url(r'^publish/',views.publish,name="publish"),
    url(r'^taginfo/(?P<tag_pk>.*?)$',views.tagInfo,name="taginfo"),
    url(r'^detail/(?P<title_pk>\d+)',views.detail,name='detail'),
]