from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^main$', views.main, name="main"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^save/(?P<id>\d+)$', views.save, name="save"),
    url(r'^add/$', views.add, name="add"),
    url(r'^add_item$', views.add_item, name="add"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^shared/(?P<id>\d+)$', views.shared_user, name="shared_user"),
    ]
