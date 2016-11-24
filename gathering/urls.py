from django.conf.urls import url
from django.conf.urls import include
from gathering import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^show_table_detail/$', views.show_table_detail, name='show_table_detail'),
    url(r'^fill_table/$', views.fill_table, name='fill_table'),
]
