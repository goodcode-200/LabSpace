from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reg$', views.reg),
    url(r'^reg_deal$',views.deal_reg),
    url(r'^login$', views.login),
    url(r'^login_deal$',views.deal_login),
    url(r'^user_logout$',views.user_logout),
    url(r'^get_nickname/(?P<nickname>.*?)$',views.get_nickname),
    url(r'^test$',views.test),
]