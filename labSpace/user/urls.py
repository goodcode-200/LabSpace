from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^account/',views.account,name='account'),
	url(r'^register/',views.register,name='register'),
	url(r'^login/',views.userLogin,name='login'),
]