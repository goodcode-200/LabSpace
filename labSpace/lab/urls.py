from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list$',views.list_lab),
    url(r'^apply$',views.apply),
    url(r'^space/(?P<space>.*?)/(?P<index>.*?)/$',views.to_space),
    url(r'^spac/(?P<space>.*?)/$',views.change_to_space),
    url(r'^get_address/(?P<address>.*?)$',views.get_address),
    url(r'^apply_deal$',views.apply_deal),
    url(r'^apl/(?P<space>.*?)/$',views.apl),
    url(r'^apl_deal/(\d+)$',views.apl_deal),
    url(r'^apl_del/(\d+)$',views.apl_del),
]