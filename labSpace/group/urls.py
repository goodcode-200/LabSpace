from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$",views.home,name="home"),
	url(r"^detail(?P<pk>\d+)$",views.labDetail,name="detail"),
]